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
        print("Query is executed - ",query)
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

conn = connect('app.db')

# insert one user record - query 3
# query3 = "INSERT INTO users(name,age) VALUES('Suresh',25)"
# execute(conn,query3)

# insert one counter record - query 4
# query4 = "INSERT INTO counter(item,counter) VALUES('orange',1)"
# execute(conn,query4)

# fetch all records -  query 5
query5 = "SELECT * from counter"
result = fetchall(conn,query5)
print(result)

# fetch one row -  query 6
query6= "SELECT * from users WHERE name='Prashanth'"
result = fetchone(conn,query6)
print(result)

# fetch one column - query 7
query7 = "SELECT name FROM users"
result = fetchall(conn,query7)
print(result)


# fetch one attribute from one row - query 8
query8 = "SELECT * FROM counter WHERE item='apple'"
result = fetchone(conn,query8)
print(result)

