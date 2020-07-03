## Conditional Statements

a,b=10,20

# if, else, elif
if a < b :
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else :
    print(f"{a} is less than {b}")

# single line code
message = "a is less than b" if a<b else "a is greater than b"
print(message)

