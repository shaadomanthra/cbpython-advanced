# Write a program to replace spaces with hypens

# input: hello every one
# output hello-every-one

str = input("Enter the string: ")
str2 = str.split(' ')
s = '-'.join(str2)
print(s)
# s = ''
# for i in str2:
#     s = s + i + '-'
# print(s)