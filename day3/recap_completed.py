## Day2 recap concepts
import sys

# variables
a = 10
print(a)
a = 'Teja'
print(a)

# getting the datatype of varaible
print(type(a))

# strings
message = "The string  is {}".format(a)
print(message)

message2 = f"Shortform - {a}"
print(message2)

# take input from commandline
name = sys.argv[1]
print(name)