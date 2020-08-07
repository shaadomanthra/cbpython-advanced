from models.db import *

class BarModel:


    def insertBarcode(self,text,username):
        conn = connect("app.db")
        query = f"INSERT into barcodes (text,username) VALUES ('{text}','{username}')"
        execute(conn,query)



