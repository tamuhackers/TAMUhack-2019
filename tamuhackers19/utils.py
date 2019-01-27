
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


def send_email(data: str) -> None:
	"""Send an email to the prospective customer.
	Parameters
	----------
	data : str
		The data for the email to be sent.
	"""

	body = """
	== Accident Information ==\r\n
	Date: {0}\r\n
	Time: {1}\r\n
	Location: {2}\r\n
	Direction of Plaintiff: {3}\r\n
	Direction of Defendent: {4}\r\n
	Weather: {5}\r\n
	Visitibility: {6}\r\n
	
	== Reported Third-Party Information ==\r\n
	Legal Name: {7}\r\n
	Phone Number: {8}\r\n
	Address: {9}\r\n
	Insurance Company {10}\r\n
	Insurance Email {11}\r\n
	VIN {12}\r\n
	""".format(
		data["date"],
		data["time"],
		data["location"],
		data["direction_you"],
		data["direction_them"],
		data["snapshot"],
		data["weather"],
		data["visibility"],
		

		data["legal_name"],
		data["phone_number"],
		data["address"],
		data["insurance_company"],
		data["insurance_email"],
		data["vin"],
	)

	# For testing purposes the sender is also the receiver
	from_address = os.environ.get("EMAIL_USER")
	email = from_address

	try:
		msg = MIMEMultipart()
		msg["From"] = from_address
		msg["To"] = email
		msg["Subject"] = "Report A Crash - Incident Report"
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