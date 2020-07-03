## Program to check if the given number is prime
import sys

def prime(num):
    for i in range(2,num):
        if num % i ==0:
            return 0
    return 1

# Read the command line input
num = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# Check for Prime
print("Prime" if prime(num) == 1 else "Not Prime")