## Basic math functions

# addition
def add(a,b):
    return a+b

# subtraction
def subtract(a,b):
    return a - b

# multiply
def multiply(a,b):
    return a*b

# power
def power(a,n):
    return a**n

# summation (varaible arguments)
def summation(*args):
    result = 0
    for i in args:
        result = result + i
    return result


# cumulative multiply (variable aarguments)
def mul(*args):
    result = 1
    for i in args:
        result = result * i
    return result
