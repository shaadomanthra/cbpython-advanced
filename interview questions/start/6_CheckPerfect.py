# Write a python program to check if the given number is perfect

def perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        print("It is a perfect number")
    else:
        print("It is not a perfect number")

num = int(input("Enter one number: "))
perfect(num)
