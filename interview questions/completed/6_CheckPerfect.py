## Program to check if the given number is perfect
'''
    Perfect - a positive integer that is equal to the sum of its proper divisors.

    For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6,
    so 6 is a perfect number

    eg: 6, 28, 496, 8128
'''

# function to check perfect
def perfect(num):
    divisorSum = 0
    for i in range(1,num):
        if num % i == 0:
            divisorSum = divisorSum + i
    if divisorSum == num:
        return 1
    else:
        return 0

# Take input from user
num = int(input("Enter the number:"))

# Check for Perfect
if perfect(num):
    print("Perfect Number")
else:
    print("it is not a Perfect Number")