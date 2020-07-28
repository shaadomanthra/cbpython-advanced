# Consider the below series:
#
# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ...
#
# This series is a mixture of 2 series - all the odd terms in this series form a Fibonacci series
# and all the even terms are the prime numbers in ascending order.
#
# Write a program to find the Nth term in this series.
#
# The value N is a Positive integer that should be read from STDIN. The Nth term that is
# calculated by the program should be written to STDOUT. Other than the value of Nth term,
# no other characters/strings or message should be written to STDOUT.
#
# For example, when N = 14, the 14th term in the series is 17. So only the value 17
# should be printed to STDOUT.

def checkEven(num):

    if num % 2 ==0
        return 1
    else
        return 0

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def Prime(num):
    i = 2
    counter = 0
    while(counter<num):
        if isPrime(i):
            counter = counter +1
        i = i + 1
    return i - 1




