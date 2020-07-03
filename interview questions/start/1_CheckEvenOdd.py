# Write a python program to check of the given number is even or odd
import sys
#
# num = int(sys.argv[1]) if len(sys.argv)>1 else 1
num = int(input("Enter one interger"))
result = "Even" if num % 2 == 0 else "Odd"
print(result)

