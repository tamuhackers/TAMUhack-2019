
from typing import Union
from uuid import uuid4

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


	def user_exists(self, phone_number: str) -> bool:
		"""Returns a boolean denoting if there is a
		user in the database associated with a given 
		phone number."""
		documents = self.db.collection("users").get()
		for document in documents:
			if document["phone_number"] == phone_number:
				return True
		return False


	def get_user(self, phone_number: str) -> Union[dict, None]:
		"""Find the user who's database entry matches a given phone number.

		Assumes there can only ever be one account associated with a phone
		number."""

		users_ref = self.db.collection("users")
		query = users_ref.where("phone_number", "==", phone_number)
		return next(query.get())._data


	def set_login_code(self, phone_number: str):
		"""Given a phone number, associate a login code for that
		number so that a user may login via SMS authentication password.
		"""
		code = str(uuid4())[-6:]
		data = {
			"phone_number": phone_number,
			"code": code,
		}
		self.db.collection("passwordless").document().set(data)
		return code


	def get_login_code(self, phone_number: str) -> str:
		"""Given a phone number, get the login code that was previously
		associated with it.

		Assumes that set_login_code was previously called and there
		is a valid value for the phone_number in the collection.
		"""
		passwordless_ref = self.db.collection("passwordless")
		query = passwordless_ref.where("phone_number", "==", phone_number)
		try:
			code = next(query.get())._data["code"]
			return code
		except StopIteration as e:
			return code


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

	"""
	# Retrive the user that was just inserted by using their phone number
	user_data = dbc.get_user(data["phone_number"])
	print(user_data)
	"""

	# Test passwordless authentication
	dbc.set_login_code(data["phone_number"])
	passwordless_code = dbc.get_login_code(data["phone_number"])
	print(passwordless_code)
	assert type(passwordless_code) == str
	assert passwordless_code is not None