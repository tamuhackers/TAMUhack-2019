
from tamuhackers19.db.cars_schema import CarsSchema
from tamuhackers19.db.users_schema import UsersSchema

from google.cloud import firestore
from marshmallow.exceptions import ValidationError


class FirestoreConnector(object):
	def __init__(self):
		self.db = firestore.Client()

	
	def register_user(self, data: dict) -> int:
		"""Given a dictionary of data, create a new document
		in the `users` collection of the Firestore database

		Returns
		--------
		int
			Possible error codes
		"""
		self.db.collection("users").document().set(data)

if __name__== "__main__":
	# Example of how the backend will read and send data to the database

	# Setup sample data
	# Model, make, and year will be provided by the smartcar API
	car_info = {
		"model": "Model 3",
		"make": "Tesla",
		"year": 2019,
		"vin": "1N4BA41E94C895344",
        "registration_class_code": "PAS",
		"license_plate": "6JTR1E",
	}
	
	try:
		car_info, error = CarsSchema(strict=True).load(car_info)
		print("Car information:", car_info)
	except ValidationError as e:
		print(e)
	
	data = {
		"legal_name": "Simon Woldemichael",
		"phone_number": "555-555-555",
		"address": "1 Main St.",
		"insurance_company": "State Farm",
		"insurance_email": "statefarm@statefarm.com",
		"car_info": car_info,
	}

	try:
		data, error = UsersSchema(strict=True).load(data)
		print("User information:", data)
	except ValidationError as e:
		print(e)
	
	# Initailize database
	dbc = FirestoreConnector()

	# Register new user with sample car information
	dbc.register_user(data)