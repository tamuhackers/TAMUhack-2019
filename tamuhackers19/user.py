from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, phone_number):
        self.phone_number = phone_number
