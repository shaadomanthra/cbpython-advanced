#  import libraries
import sqlite3
from sqlite3 import Error

# create connection
def connect(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)

def execute(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        print("Executed the query -", query)
        conn.commit()
        conn.close()
    except Error as e:
        print(e)


# close connection
def close(conn):
    try:
        conn.close()
    except Error as e:
        print(e)

conn = connect("app.db")
query1 = "CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, age INTEGER)"
execute(conn,query1)

query2 ="CREATE TABLE counter (id INTEGER PRIMARY KEY AUTOINCREMENT,item TEXT, counter INTEGER)"
execute(conn,query2)
close(conn)



