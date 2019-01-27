import os#, db

from flask import Flask, redirect, url_for, render_template, request
from flask_mail import Mail


os.environ["FLASK_ENV"] = "development"
app = Flask(__name__)
mail = Mail(app)

SENDER = "carinsurance@gmail.com"
PASSWORD = "smart_insurance"

# dbc = FirestoreConnector()

# def getLightInfo():
# 	return dbc.vehicle[0]

# def getemergencyInfo():
# 	return dbc.vehicle[0] + " " + dbc.vehicle[0]

# Home
@app.route('/', method=["POST","GET"])
def home():
	if request.method == "POST":
		info = ()
		# Send info and redirect in case of emergency accident
		if request.form["emergency"] == True:
			insurance(request.form,"emergency")
			return redirect('/emergency', info=info)
		# Send info and redirect in case of light accident
		elif request.form["light"] == True:
			return redirect('/light', info=info)
		elif request.form["profile"] == True:
			return redirect('/profile')

# Sending insurance email
def insurance(info, type):
	insurNum = ""

	# Send email to insurance company
	if info[10] != ""
		subject = info[10]
	else
		subject = "IMPORTANT: CRASH!" + insurNum

	if info[11] != ""
		body = info[""]
	else
		body = "I have just gotten in a " + type " crash. Please call " + info[3] + " and email at " + info[4] + "."

	sender = SENDER

	msg = Message(recipients=info[1], subject=subject, body=body)
	# Exchange information of both drivers from the database (use access codes?)

# Emergency
@app.route('/emergency', method="POST")
def emergency(info=info):
	insurance(info, type="emergency")
	# Call police

# Light
@app.route('/light', method="POST")
def light():
	insurance(info, type="light")


# Profile
@app.route('/profile', method="POST")
def profile():
	if request.method == "POST":

		data = {
        "model": ,
        "make": "Tesla",
        "year": 2019,
        "registration_class_code": "PAS",
        "vin": "1N4BA41E94C895344",
        "license_plate": "6JTR1E",
	    }
    	try:
        	data, error = CarsSchema(strict=True).load(data)
        	print(data)
	    except ValidationError as e:
	        print(e)

		data = {
        "model": ,
        "make": "Tesla",
        "year": 2019,
        "registration_class_code": "PAS",
        "vin": "1N4BA41E94C895344",
        "license_plate": "6JTR1E",
	    }
    	try:
        	data, error = CarsSchema(strict=True).load(data)
        	print(data)
	    except ValidationError as e:
	        print(e)

	# Send email to insurance company
	# Exchange information of both drivers from the database (use access codes?)