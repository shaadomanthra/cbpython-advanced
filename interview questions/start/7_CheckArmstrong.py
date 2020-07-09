# Write a python program to check if the given number is armstrong

def armstrong(num):
    sum =0
    temp = num
    while temp:
        digit  = temp % 10 # capturing last digit
        sum  = sum + digit ** 3 # cube is num ** 3
        temp = temp // 10
    if sum == num:
        print("Armstrong number")
    else:
        print("It is not Armstrong")

num = int(input("Enter the number: "))
armstrong(num) # 153

# lastdigit = num % 10
# print(f"The last digit in {num} is {lastdigit}")