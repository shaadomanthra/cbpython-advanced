# Program to calculate the factorial of given number

num = int(input("Enter the number: "))

factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
    print(i,factorial)

print(f"The factorial of {num} is {factorial}")
