import os#, db

from flask import Flask, redirect, url_for, render_template, request
from flask_mail import Mail


os.environ["FLASK_ENV"] = "development"
app = Flask(__name__)
mail = Mail(app)

# dbc = FirestoreConnector()

# def getLightInfo():
# 	return dbc.vehicle[0]

# def getSevereInfo():
# 	return dbc.vehicle[0] + " " + dbc.vehicle[0]

# Home
@app.route('/home', method=["POST","GET"])
def home():
	if request.method == "POST":
		# Send info and redirect in case of severe accident
		if request.form["severe"] == True:
			# info = dbc.getSevereInfo()
			return redirect('/severe', info=info)
		# Send info and redirect in case of light accident
		elif request.form["light"] == True:
			# info = dbc.getLightInfo()
			return redirect('/light', info=info)
		elif request.form["profile"] == True:
			return redirect('/profile')

# Sending insurance email
def insurance(info=info, type=type):
	insurNum = info[5]

	# Send email to insurance company
	if info[10] != ""
		subject = info[10]
	else
		subject = "IMPORTANT: CRASH!" + insurNum

	if info[11] != ""
		body = info[11]
	else
		body = "I have just gotten in a " + type " crash. Please call " + info[3] + " and email at " + info[4] + "."

	msg = Message(sender=info[0], recipients=info[1], subject=subject, body=body)
	# Exchange information of both drivers from the database (use access codes?)

# Severe
@app.route('/severe', method=["POST","GET"])
def severe(info=info):
	insurance(info, type="severe")
	# Call police

# Light
@app.route('/light', method=["POST","GET"])
def light():
	insurance(info, type="light")


# Profile
@app.route('/profile', method=["POST","GET"])
def profile():
	if request.method == "POST":
		dbc.setInfo
		return redirect('/home')
	elif request.method == "GET":
		dbc.getInfo

	# Send email to insurance company
	# Exchange information of both drivers from the database (use access codes?)