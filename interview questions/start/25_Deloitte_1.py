# Write a program to print reverse substring of first four letters of the given input
# eg input : indianocean, output: idni

str = input("Enter a string: ")
str_new = str[0:4]
print(str_new[::-1])