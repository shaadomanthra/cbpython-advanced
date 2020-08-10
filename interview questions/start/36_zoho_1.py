# write a program to print string removing vowels
# eg: input : apple , output : ppl

l = ['a','e','i','o','u']

str = input("Enter the string: ")

for s in str:
    if s not in l:
        print(s)