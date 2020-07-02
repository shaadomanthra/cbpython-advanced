# Write a python program to convert m/s to km/hr

#Import packages
import sys

# Read the command line input
mps = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# Conversion Logic
kmph = mps * 3.6
result = round(kmph,1)

# display result
print(result)