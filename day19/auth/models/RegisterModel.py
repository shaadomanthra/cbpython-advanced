from models.db import *

class RegisterModel:

    def create(self):
        conn = connect("app.db")
        print("Database created")

    def save(self,name,email,password):
        conn = connect('app.db')
        query = f"INSERT INTO users(name,email,password) VALUES('{name}','{email}','{password}')"
        execute(conn,query)
        print("One record inserted")

