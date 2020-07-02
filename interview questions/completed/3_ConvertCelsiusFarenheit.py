# Write a python program to convert Celsius to Farenheit

#Import packages
import sys

# Read the command line input
celsius = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# Conversion Logic
farenheit = (celsius * 1.8 ) + 32
result = round(farenheit,2)

# display result
print(result)