from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, phone_number, code):
        self.user_id = phone_number
        self.code = code

    def get_id(self):
        return self.user_id