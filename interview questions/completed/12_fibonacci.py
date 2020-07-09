"""
    # Program to print the fibonacci series
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""

def fibonacci(n):
    """The fibonacci() function prints the fibonacci series"""
    if n < 0:
        print("Incorrect input")
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c

# Read the input from user
num = int(input("Enter the number of elements in fibonacci series: "))

fibonacci(num)