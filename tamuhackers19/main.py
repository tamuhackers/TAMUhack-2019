# -*- coding: utf-8 -*-

import os
import datetime

from uuid import uuid4
from typing import Union

from flask import Flask, jsonify, render_template, redirect, request, session, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from tamuhackers19.db.firestore_client import FirestoreConnector
from tamuhackers19.user import User
from tamuhackers19.utils import send_text_message

import smartcar
import requests

client = smartcar.AuthClient(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    redirect_uri=os.environ.get('REDIRECT_URI'),
    scope=['read_vehicle_info','read_vin','read_odometer','read_location','control_security', 'control_security:unlock', 'control_security:lock'],
    test_mode=True,
)

app = Flask("tamuhack19", template_folder=f"{os.path.dirname(os.path.realpath(__file__))}/templates")
app.secret_key = uuid4().hex
access = None
info = None

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

dbc = FirestoreConnector()

@login_manager.user_loader
def user_loader(user_id) -> Union[User, None]:
    if user_id == dbc.get_login_code(user_id):
	    user = User(user_id, request.form["code"])
	    return user
    return


@login_required
@app.route("/", methods = ["GET"])
def home():
    return render_template("home.html", car_data="Please Authenticate by Logging In")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_anonymous:
        if request.method == "POST":
            phone_number = request.form["phone_number"]
            if "code" not in request.form:
                # User is attempting to log in using passwordless authentication
                send_text_message(f"Your access code is {dbc.set_login_code(phone_number)}")
                return render_template("sms.html", phone_number=phone_number)
            elif "code" in request.form:
                code = dbc.get_login_code(phone_number)
                if request.form["code"] == code:
                    # User submitted the correct code and may login
                    user = User(phone_number, code)
                    login_user(user)
                    print("User successfully logged in.")
                    auth_url = client.get_auth_url()
                    return redirect(auth_url)
        return render_template("login.html")
    return "You are already logged in!"

@app.route("/profile", methods = ["GET"])
def profile():
    # Sample placement data
    placement = {
        "legal_name": "John Doe",
        "phone_number": "555-555-5555",
        "address": "aaaa",
        "insurance_company":"State Farm",
        "insurance_email": "statefarm@statefarm.com",
        "license_plate": "99999",
        "make": "Tesla",
        "model": "Model",
        "year": "Year",
        "registration_class_code": "PAS",
        "vin": "AAAAAAAAAAAAAAAAAAAA"
        }

    return render_template("profile.html", 
        name = placement["legal_name"], 
        p_num = placement["phone_number"], 
        a = placement["address"], 
        insurance = placement["insurance_company"], 
        ins_email = placement["insurance_email"], 
        plate = placement["license_plate"], 
        make = placement["make"] if info is None else info["make"], 
        model = placement["model"] if info is None else info["model"], 
        year = placement["year"] if info is None else info["year"], 
        rcc = placement["registration_class_code"], 
        vin = placement["vin"] if info is None else info["vin"]
    )


@app.route("/light", methods = ["GET", "POST"])
def light():
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    time = datetime.datetime.today().strftime('%H:%M')
    if request.method == "POST":
        data = {
            # Meta data of the crash
            "date": request.form["date"],
            "time": request.form["time"],
            "location": request.form["location"],
            "direction_you": request.form["direction_you"],
            "direction_them": request.form["direction_them"],
            "snapshot": request.form["snapshot"], # Might need to double check that this gets base encoded
            "weather": request.form["weather"],
            "visibility": request.form["visibility"],
            
            # The information of the other party involved
            "legal_name": request.form["legal_name"],
            "phone_number": request.form["phone_number"],
            "address": request.form["address"],
            "insurance_company": request.form["insurance_company"],
            "insurance_email": request.form["insurance_email"],
            "vin": request.form["vin"],
            "model": request.form["model"],
            "make": request.form["make"],
            "year": request.form["Year"], # Double check captial 'y' here
            "license_plate": request.form["license_plate"],
            "registration_class_code": request.form["registration_class_code"],
        }
        # Now check for the optional data
        if "has_witness" in request.form:
            data["has_witness"] = True
            data["witness_legal_name"] = request.form["witness_legal_name"]
            data["witness_phone_number"] = request.form["witness_phone_number"]
            data["witness_testimony"] = request.form["witness_testimony"]
        if "has_police" in request.form:
            data["has_police"] = True
            data["police_legal_name"] = request.form["police_legal_name"]
            data["police_badge"] = request.form["police_badge"]
        response = requests.post('http://127.0.0.1:5002/light', data=data)
        print(response)
    var info =  {'id': '25b0759f-be63-42c4-84f7-662efa180a15', 'make': 'TESLA', 'model': 'Model 3', 'year': 2018, 'location': {'data': {'latitude': 40.84291076660156, 'longitude': -105.43253326416016}, 'age': datetime.datetime(2019, 1, 27, 14, 56, 55, 210000, tzinfo=tzutc())}, 'vin': '76DFCF78A4130F34B', 'odometer': {'data': {'distance': 68968.84375}, 'unit_system': 'metric', 'age': datetime.datetime(2019, 1, 27, 14, 56, 55, 764000, tzinfo=tzutc())}}
    return render_template("light.html", d = date, t = time, l=info['location']['data'] if info is not None else "Please Authenticate by Logging in")


@app.route("/logout")
def logout():
    if not current_user.is_anonymous:
        logout_user()
        print("Logged out user.")
        return redirect(url_for("login"))
    print("There is no user available in the session.")
    return redirect(url_for("login"))


@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')

    # TODO: Request Step 1: Obtain an access token
    # access our global variable and store our access tokens
    global access
    # in a production app you'll want to store this in some kind of
    # persistent storage
    access = client.exchange_code(code)
    print(access)
    return redirect(url_for("vehicle"))


@app.route('/vehicle', methods=['GET'])
def vehicle():
    # access our global variable to retrieve our access tokens
    global access
    # the list of vehicle ids
    vehicle_ids = smartcar.get_vehicle_ids(access["access_token"])['vehicles']
    
    # TODO: Request Step 3: Create a vehicle    
    # instantiate the first vehicle in the vehicle id list
    vehicle = smartcar.Vehicle(vehicle_ids[0], access['access_token']) #Get vehicle general info

    global info
    info = vehicle.info()

    info["location"] = vehicle.location()
    info["vin"] = vehicle.vin()
    info["odometer"] =  vehicle.odometer()
    print(info)
    return render_template("home.html", car_data=info)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 80
    print(f"Initializing application on {host}:{port} ")
    app.run(host=host, port=port)