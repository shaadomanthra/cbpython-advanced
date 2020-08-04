# Write a program to find the sum of cubes of nuturals numbers upto n.
# The number 'n' is given by user

num = int(input("Enter one natural number: "))

sum = 0
for i in range(1,num+1):
    sum = sum + (i * i * i)

print("The sum of the cubes of the natural numbers is :",sum)


