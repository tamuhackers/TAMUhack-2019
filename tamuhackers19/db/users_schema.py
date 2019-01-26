from marshmallow import Schema, fields

from tamuhackers19.db.cars_schema import CarsSchema

class UsersSchema(Schema):
    legal_name = fields.String()
    phone_number = fields.String()
    address = fields.String()
    insurance_company = fields.String()
    insurance_email = fields.String()
    car_info = fields.Nested(CarsSchema, strict=True)
    
    
if __name__ == "__main__":
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
