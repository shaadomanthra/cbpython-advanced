## Program to check if the given number is prime

# function to check if num is prime
def prime(num):
    for i in range(2,num):
        if num % i ==0:
            return 0
    return 1

# Take input from user
num = int(input("Enter the number:"))

# Check for Palindrome
if prime(num):
    print("Prime")
else:
    print("Not prime")