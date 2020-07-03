# Write a python program to convert Mps to Kmph
# mps = int(input("Enter speed in m/s:"))

import sys

mps = int(sys.argv[1]) if len(sys.argv)>1 else 1
kmph = round(mps * 3.6,2)
print(f"The speed in kmph is {kmph}")
