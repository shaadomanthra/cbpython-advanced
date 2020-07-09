"""
    # Program to Swap two numbers
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""


def swap(a, b):
    """The swap() function prints the swapped numbers"""
    print(f"The given numbers are {a} and {b}")
    a, b = b, a
    print(f"The swapped numbers are {a} and {b}")


# Read the input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

swap(a, b)
