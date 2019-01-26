from pprint import pprint

from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

class CarsSchema(Schema):
    model = fields.String()
    make = fields.String()
    year = fields.Integer()
    vin = fields.String()
    license_plate = fields.String()


if __name__ == "__main__":
    data = {
        "model": "Model 3",
        "make": "Tesla",
        "year": 2019,
        "vin": "1N4BA41E94C895344",
        "license_plate": "6JTR1E",
    }
    try:
        data, error = CarsSchema(strict=True).load(data)
    except ValidationError as e:
        print(e)