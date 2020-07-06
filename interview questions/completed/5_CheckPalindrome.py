## Program to check if the given number is palindrome
'''
    Palindrome - An integer is a palindrome if the reverse of that number is equal
                to the original number.
'''

# function to check palindrome
def palindrome(num):

    reverseNumber = 0
    originalNumber = num
    while num !=0:
        lastDigit = num % 10
        reverseNumber = reverseNumber * 10 + lastDigit
        num = int(num / 10)
    if reverseNumber == originalNumber:
        return 1
    else:
        return 0

# Take input from user
num = int(input("Enter the number:"))

# Check for Palindrome
if palindrome(num):
    print("Palindrome")
else:
    print("Not palindrome")