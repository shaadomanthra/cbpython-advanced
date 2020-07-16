'''
    Write python code for the below
    1. Create a database 'new.db'
    2. Add table users with field id,name,email,password,age
    3. insert three users
    4. fetch row with id 2
    5. fetch all the ages
    6. fetch one person email
'''
from db import *


# 1. Create a database 'new.db'
connection = connect('new.db')

# 2. Add table users with field id,name,email,password,age
# query1 = "CREATE TABLE users (id integer PRIMARY KEY AUTOINCREMENT, name text, email text, password text,age integer)"
# execute(connection,query1)

# 3. insert three users
# query2 = "INSERT INTO users (name,email,password,age) VALUES ('Suresh','suresh@packetprep.com','suresh123', 50)"
# execute(connection,query2)

# 4. fetch row with id 2
query3 = "SELECT * FROM users WHERE id = 2"
result = fetchone(connection,query3)
print(result)

# 5. fetch all the ages
query4 = "SELECT age FROM users"
result = fetchall(connection,query4)
print(result)

# 6. fetch one person email
query5 = "SELECT email FROM users WHERE name = 'Suresh'"
result = fetchone(connection,query5)
print(result)

# update the record
query6 = "UPDATE users SET password = 'sample123' WHERE name='Rajesh'"
execute(connection,query6)

query7 = "SELECT password FROM users WHERE name = 'Rajesh'"
result = fetchone(connection,query7)
print(result)

# update first records age to 100
query8 = "UPDATE users SET age = 100 WHERE id=1"
execute(connection,query8)

# DELETE a record
query9 = "DELETE FROM users WHERE age=40"
execute(connection,query9)

# DELETE record where id = 1
query10 = "DELETE FROM users WHERE id = 1"
execute(connection,query10)




