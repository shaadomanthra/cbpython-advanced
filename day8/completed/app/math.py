## Basic math functions

# addition
def add(a,b):
    return a+b

# subtraction
def subtract(a,b):
    return a-b

# multiply
def multiply(a,b):
    return a*b

# power
def power(a,b):
    return a**b

# summation
def summation(*args):
    result =0
    for i in args:
        result = result + i
    return result

# cumulative multiply
def mul(*args):
    result =1
    for i in args:
        result = result * i
    return result
