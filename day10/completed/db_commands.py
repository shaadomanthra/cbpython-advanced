import sqlite3
from sqlite3 import Error


def connect(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)

def execute(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Successfully executed - ",query)
        cursor.close()
    except Error as e:
        print(e)

def fetchone(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchone()
        cursor.close()
        return record
    except Error as e:
        print(e)

def fetchall(conn,query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except Error as e:
        print(e)


def close(conn):
    try:
        conn.close()
    except Error as e:
        print(e)


conn = connect('app.db')
# create users table
query1 = "CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT, name text, age integer)"
execute(conn,query1)

# create counter table
query2 = "CREATE TABLE counter (id integer PRIMARY KEY AUTOINCREMENT, item text, counter integer)"
execute(conn,query2)

# insert one user record
# query3 = "INSERT INTO users (name,age) VALUES ('Rajesh',30)"
# execute(conn,query3)

# # insert one counter record
# query4 = "INSERT INTO counter (item,counter) VALUES ('orange',1)"
# execute(conn,query4)

# fetch all records
query5 = "SELECT * FROM users"
result = fetchall(conn,query5)
print(result)

# fetch one row
query6 = "SELECT * FROM users WHERE id =1"
result = fetchone(conn,query6)
print(result)

# fetch one column
query7 = "SELECT name FROM users"
result = fetchall(conn,query7)
print(result)

# fetch one attribute from one row
query7 = "SELECT name FROM users WHERE id =1"
result = fetchone(conn,query7)
print(result[0])

# # update a user record
# query5 = "UPDATE users SET age=45 WHERE id =1"
# execute(conn,query5)
#
# # update a counter record
# query6 = "UPDATE counter SET counter=10 WHERE item='apple'"
# execute(conn,query6)

# delete a record
# query7 = "DELETE FROM users WHERE id = 2"
# execute(conn,query7)

close(conn)