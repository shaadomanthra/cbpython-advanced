from db import *

class model:

    def insert(self,name,count):
        conn = connect('app.db')
        query = f"INSERT INTO counter (name,count) VALUES('{name}',{count})"
        execute(conn,query)
        print("The record is inserted")

