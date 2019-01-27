import os#, db

from flask import Flask, redirect, url_for, render_template, request

from tamuhackers19.db.firestore_client import FirestoreConnector

app = Flask("AccidentAppBackend")


dbc = FirestoreConnector()

"""
# Sending insurance email
def send_email(info, type):
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
"""
# Emergency
@app.route('/emergency', methods=["POST"])
def emergency():
	...
	"""Extract data from the front-end and
	Send an email to the insurance company of both
	parties involved.
	"""

	#insurance(info, type="emergency")
	# Call police

# Light
@app.route('/light', methods=["POST"])
def light():
	if request.method == "POST":
		print(1, request.form)
	return "hi", 200


# Profile
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