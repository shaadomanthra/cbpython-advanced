# Program to print the fibonacci series

def fibonacci(num):
    if num<0:
        print("Incorrect Value")
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,num):
        c = a + b
        print(c)
        a = b
        b = c

num = int(input("Enter the number of fibonnacci numbers: "))

fibonacci(num)