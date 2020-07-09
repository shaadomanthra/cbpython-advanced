"""
    # Program to count digits in a given number
    #
    # Author    -   Krishna Teja GS
    # Contact   -   founder@packetprep.com
    # Website   -   https://packetprep.com/course/python-for-interviews
"""

def countDigits(num):
    """The countDigits function counts the digits in the given number and
    retuns the count"""
    count = 0
    while num:
        num = num//10
        count=count+1
    return count

def countDigits_str_method(num):
    return len(str(num))

def countDigits_recursive(num):
    if num == 0:
        return 0
    return 1 + countDigits_method3(num//10)

# Read the input from user
num = int(input("Enter the number: "))

result = countDigits(num)
# result = countDigits_str_method(num)
# result = countDigits_recursive(num)
print(f"The number {num} has {result} digits ")