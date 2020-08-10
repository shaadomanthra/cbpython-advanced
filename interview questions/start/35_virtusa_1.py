# Write a program to print a series of 20 numbers with even positions as prime numbers
# starting from 3 and odd poisitions in AP with common difference 5 and first number 10

def isPrime(num):
    for k in range(2,num):
        if num % k == 0:
            return 0
    return 1

def listAp(start,diff,limit):
    l = []
    for i in range(0, limit):
        ap = start + (i-1)*diff
        l.append(ap)
    return l

def listPrime(start, limit):
    counter = 0
    l = []
    j = start
    while True:
        if isPrime(j)==1:
            l.append(j)
            counter = counter +1
        if counter == limit:
            break
        j = j + 1

    return l


ap_list = listAp(10,5,10)
prime_list = listPrime(3,10)

for i in range(0,10):
    print(ap_list[i])
    print(prime_list[i])

# print(ap_list)
# print(prime_list)









