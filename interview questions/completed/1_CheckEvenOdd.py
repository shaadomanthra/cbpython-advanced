## Program to check if the given number is Even or Odd
import sys

# Read the command line input
num = int(sys.argv[1]) if len(sys.argv) > 1 else 20

# Even odd Logic
message = "Even" if num % 2 == 0 else "Odd"

print(message)