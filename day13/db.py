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

# execute function
def execute(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(e)

# fetchone
def fetchone(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        cursor.close()
        return record
    except Error as e:
        print(e)

# fetchall
def fetchall(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except Error as e:
        print(e)

# close connection
def close(conn):
    try:
        conn.close()
    except Error as e:
        print(e)