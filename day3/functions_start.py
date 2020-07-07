# # Functions in Python

# Basic function
def basic():
    print("This is basic function")

basic()
# function with arguments
def sum(a,b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

sum(30,40)

# function with return value
def subtract(a,b):
    res = a-b
    return res

result = subtract(100,20)
print(f"The subtraction of two number is {result}")

# function with default value
def subtract(a,b=20):
    res = a-b
    return res

result = subtract(50,30)
print(f"The subtraction of two number is {result}")

# function with varaible arguments

# global & local variables
