import os
import smtplib
import datetime

from flask import Flask, redirect, url_for, render_template, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from smartcarAPI import vehicle

app = Flask(__name__)


@app.route("/")
def get_data():
	"""Send an email to the prospective customer.
	Parameters
	----------
	email : str
		The email that was submitted.
	body : str
		The body of the email to be sent.
	""" 

	from_address = "reportacrashinfo@gmail.com"
	email = ""

	try:
		msg = MIMEMultipart()
		msg["From"] = from_address
		msg["To"] = email
		msg["Subject"] = "Test"
		body = "Test occured on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")# + " " + vehicle() 
		msg.attach(MIMEText(body, "plain"))
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login("reportacrashinfo@gmail.com", "tamureportacrash")
		server.sendmail(from_address, [from_address,"reportacrashinfo@gmail.com"], msg.as_string())
		server.quit()
	except Exception as e:
		print(e)

	return ""

	
if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Initializing application on {host}:{port} ")
    app.run(host=host, port=port)