import sqlite3
from sqlite3 import Error


def connect(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)

def close(conn):
    try:
        conn.close()
    except Error as e:
        print(e)

conn = connect('app.db')
close(conn)



