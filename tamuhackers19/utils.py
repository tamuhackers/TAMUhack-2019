
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from twilio.rest import Client
from tamuhackers19.db.firestore_client import FirestoreConnector

def send_text_message(message: str) -> None:
	"""Send testing text messages for passwordless
    authentication. Currently only sends to free Twilio.
	"""
	Client().messages.create(
		to=os.environ.get("TWILIO_TARGET"), 
		from_=os.environ.get("TWILIO_NUMBER"),
		body=message,
	)

def send_email(email: str, data: str) -> None:
	"""Send an email to the prospective customer.
	Parameters
	----------
	email : str
		The email that was submitted.
	data : str
		The data of the email to be sent.
	""" 
	body = data
	from_address = os.environ.get("EMAIL_USER")
	try:
		msg = MIMEMultipart()
		msg["From"] = from_address
		msg["To"] = email
		msg["Subject"] = "ReportACrash - Incident Report"
		msg.attach(MIMEText(body, "plain"))
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(from_address, os.environ.get("EMAIL_PASS"))
		server.sendmail(from_address, [from_address, email], msg.as_string())
		server.quit()
	except Exception as e:
		pass


if __name__ == "__main__":
    dbc = FirestoreConnector()
    dbc.set_login_code("832-630-6644")
    send_text_message(f"Your verification code is {dbc.get_login_code('832-630-6644')}")