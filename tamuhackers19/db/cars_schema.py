from pprint import pprint

from marshmallow import Schema, fields
from marshmallow.exceptions import ValidationError

class CarsSchema(Schema):
    """
    Notes
    -----
    registration_class_code : str May be any of
      - PAS (Passenge Vehicles)
      - SRF (Personalized Plates)
      - COM (Commercial Vechicles)
      - MOT (Motorcycles)
      - HSM (Historical Motorcycles)
      - LMA, LMB, LMC (Limited Use Motorcycles)
    """
    model = fields.String()
    make = fields.String()
    year = fields.Integer()
    vin = fields.String()
    registration_class_code = fields.String()
    license_plate = fields.String()


if __name__ == "__main__":
    data = {
        "model": "Model 3",
        "make": "Tesla",
        "year": 2019,
        "registration_class_code": "PAS",
        "vin": "1N4BA41E94C895344",
        "license_plate": "6JTR1E",
    }
    try:
        data, error = CarsSchema(strict=True).load(data)
        print(data)
    except ValidationError as e:
        print(e)