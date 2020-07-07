## Write a python program to check if the given number is prime

# Prime number is divisible by 1 and itself
def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

num = int(input("Enter the number: "))
if prime(num):
    print("The given number is prime")
else:
    print("The given number is not prime")