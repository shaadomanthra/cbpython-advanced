## Exception handling in python

# basic


# Named errors
# Error Reporting
try:
    str = int("Apple")
except ValueError as e:
    print(f"Value Error - {e}")
except ZeroDivisionError as e:
    print(f"Zero Div Error - {e}")
else:
    print("All is well")

print("The program continues")



