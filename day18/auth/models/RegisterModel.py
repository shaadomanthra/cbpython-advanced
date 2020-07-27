from models.db import *

class RegisterModel:

    def create(self):
        conn = connect("app.db")
        print("Database created")