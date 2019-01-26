import os#, db

from flask import Flask, redirect, url_for, render_template, request


os.environ["FLASK_ENV"] = "development"
# dbc = FirestoreConnector()

# def getLightInfo():
# 	return dbc.vehicle[0]

# def getSevereInfo():
# 	return dbc.vehicle[0] + " " + dbc.vehicle[0]

# home
@app.route('/home', method=["POST","GET"])
def home():
	if request.method == "POST":
		# Send info and redirect in case of severe accident
		if request.form["severe"] == true:
			# info = dbc.getSevereInfo()
			return redirect('/emergency', info=info)
		# Send info and redirect in case of light accident
		elif request.form["light"] == true:
			# info = dbc.getLightInfo()
			return redirect('/light', info=info)
		elif request.form["profile"] == true:
			return redirect('/profile')
	else:
		abort