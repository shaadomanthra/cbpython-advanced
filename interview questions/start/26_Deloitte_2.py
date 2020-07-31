# Write a python program to add 10 subsequent prime numbers from the given prime number.

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

num = int(input("Enter a prime number:"))
counter = 0
sum = 0
while(counter!=10):
    num = num + 1
    if prime(num):
        counter = counter + 1
        sum = sum + num
        # print(nusm, sum)

print(sum)




