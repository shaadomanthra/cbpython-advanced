## Write a python program to check if the given number is palindrome

# palindrome is a number if its reverse is equal to the original number
#  eg: 353, 55644655

def palindrome(num):
    num = str(num)
    reverse = num[::-1]
    print(reverse,num)
    if reverse == num:
        return 1
    else:
        return 0

print(palindrome(343))