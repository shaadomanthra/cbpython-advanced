from models.db import *

class LoginModel:

    def getUser(self,email,password):

        conn = connect('app.db')
        query = f"SELECT * FROM users WHERE email='{email}' and password='{password}'"
        result = fetchone(conn,query)
        return result