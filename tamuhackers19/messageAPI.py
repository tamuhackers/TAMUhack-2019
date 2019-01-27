import os
<<<<<<< HEAD
import smtplib
import datetime

from flask import Flask, redirect, url_for, render_template, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tamuhackers19.db.firestore_client import FirestoreConnector
=======

from flask import Flask, redirect, url_for, render_template, request
>>>>>>> origin/master

from tamuhackers19.db.firestore_client import FirestoreConnector
from tamuhackers19.utils import send_email

<<<<<<< HEAD
os.environ["FLASK_ENV"] = "development"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tamu.json"
app = Flask(__name__)

SENDER = "reportacrashinfo@gmail.com"
PASSWORD = "tamureportacrash"

dbc = FirestoreConnector()


# Home
@app.route('/')
def home():
	#if request.method == "POST":
	return insurance()
	# Send info and redirect in case of emergency accident
# if request.form["type"] == "emergency":
	return redirect('/emergency')
# Send info and redirect in case of light accident
# elif request.form["type"] == "light":
	return redirect('/light')
# elif request.form["type"] == "profile":
	return redirect('/profile')

# Sending insurance email
def insurance():
	insurNum = "16516515"
	# type = request.form["type"]
	# Send email to insurance company
	try:
		if request.form["custom_sub"] != "":
			subject = info[10]
		else:
			subject = "IMPORTANT: CRASH!" + insurNum

		if request.form["custom_bod"] != "":
			extra = info[""]
		else:
			extra = "I have just gotten in a " + request.form["type"] + " crash. Please call " + info[3] + " and email at " + info[4] + "."

		return "new message"
		#from_address = request.form["insurance_email"]
		from_address = "reportacrashinfo@gmail.com"
		email = ""
		msg = MIMEMultipart()
		msg["From"] = from_address
		msg["To"] = email
		msg["Subject"] = subject
		body = "Test occured on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ". " + extra
		msg.attach(MIMEText(body, "plain"))
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(SENDER, PASSWORD)
		server.sendmail(from_address, [from_address], msg.as_string())
		server.quit()
	except Exception as e:
		failed = True
		print(e)
		return str(failed) + " " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	return "hi"
	# Exchange information of both drivers from the database (use access codes?)

# Emergency
@app.route('/emergency', methods=["POST","GET"])
def emergency():
	
	return ""

# Light
@app.route('/light', methods=["POST","GET"])
def light():
=======
app = Flask("AccidentAppBackend")

dbc = FirestoreConnector()

# Emergency
@app.route('/emergency', methods=["POST"])
def emergency():
	...
	"""Extract data from the front-end and
	Send an email to the insurance company of both
	parties involved.
	"""


# Light
@app.route('/light', methods=["POST"])
def light():
	if request.method == "POST":
		data = request.form
		send_email(data)
		return "Success", 200
	return "Failure", 404
>>>>>>> origin/master

	return ""

# Profile
<<<<<<< HEAD
@app.route('/profile', methods=["POST","GET"])
def profile():
	if request.method == "POST":
		if dbc.user_exists(request.form["phone_number"])
		dbc.car_info = {
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

		dbc.data = {
			"legal_name": "Simon Woldemichael",
			"phone_number": "555-555-555",
			"address": "1 Main St.",
			"insurance_company": "State Farm",
			"insurance_email": "statefarm@statefarm.com",
			"car_info": dbc.car_info,
		}

		try:
			data, error = UsersSchema(strict=True).load(data)
			print("User information:", data)
		except ValidationError as e:
			print(e)
	return ""

	# Send email to insurance company
	# Exchange information of both drivers from the database (use access codes?)

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Initializing application on {host}:{port} ")
    app.run(host=host, port=port)
=======
@app.route('/profile', methods=["POST"])
def profile():
	if request.method == "POST":
		...
	"""
		data = {
		"model": "",
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
		"model": "",
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
	"""

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5002)
>>>>>>> origin/master
