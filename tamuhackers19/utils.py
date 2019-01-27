
import os

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

if __name__ == "__main__":
    dbc = FirestoreConnector()
    dbc.set_login_code("832-630-6644")
    send_text_message(f"Your verification code is {dbc.get_login_code('832-630-6644')}")