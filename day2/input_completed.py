# Taking input from user
import sys

# Input funtion
a = input("Enter a number")
print("you have entered",a)

# command line arguments
print(len(sys.argv))
print('The command line arguments are ',str(sys.argv))
print(sys.argv[1])
