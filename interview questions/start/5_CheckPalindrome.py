## Write a python program to check if the given number is palindrome

# palindrome is a number if its reverse is equal to the original number
#  eg: 353, 55644655

def palindrome(num):
    reverse = 0
    original = num
    while(num):
        lastdigit = num%10
        reverse = reverse * 10 + lastdigit
        num = int(num /10)
    print(reverse,original)
    if reverse == original:
        return 1
    else:
        return 0

print(palindrome(345))