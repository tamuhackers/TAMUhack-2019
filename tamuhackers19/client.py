from flask import Flask, render_template, request
import requests
import os
import datetime

os.environ["FLASK_ENV"] = "development"
os.environ['NO_PROXY'] = '127.0.0.1'

app = Flask("AccidentApp", template_folder=f"{os.path.dirname(os.path.realpath(__file__))}/templates")
@app.route("/", methods = ["GET"])
def home():
    return render_template("home.html")

@app.route("/profile", methods = ["GET"])
def profile():
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

    return render_template("profile.html", name = placement["legal_name"], p_num = placement["phone_number"], a = placement["address"], insurance = placement["insurance_company"], ins_email = placement["insurance_email"], \
                            plate = placement["license_plate"], make = placement["make"], model = placement["model"], year = placement["year"], rcc = placement["registration_class_code"], vin = placement["vin"])

@app.route("/emergency", methods = ["GET"])
def emergency():
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    time = datetime.datetime.today().strftime('%H:%M')
    if request.method == "POST":
        print(request.form)
    return render_template("emergency.html", d = date, t = time)

@app.route("/light", methods = ["GET", "POST"])
def light():
    date = datetime.datetime.today().strftime('%m-%d-%Y')
    time = datetime.datetime.today().strftime('%H:%M')
    location = "College Station"
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
            "email": request.form["email"],
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
        print(data["snapshot"])    
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
    return render_template("light.html", d = date, t = time, l = location)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001)