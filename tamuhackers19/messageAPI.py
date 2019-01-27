import os

from flask import Flask, redirect, url_for, render_template, request

from tamuhackers19.db.firestore_client import FirestoreConnector
from tamuhackers19.utils import send_email

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

	#insurance(info, type="emergency")
	# Call police

# Light
@app.route('/light', methods=["POST"])
def light():
	if request.method == "POST":
<<<<<<< Updated upstream
		data = request.form
		send_email(data)
		return "Success", 200
	return "Failure", 404
=======
		print(request.form)
	return "hi", 200
>>>>>>> Stashed changes


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