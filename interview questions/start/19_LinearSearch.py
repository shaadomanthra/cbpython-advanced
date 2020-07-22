# Write a python program to search for an element in a list

l = [20,30,45,20,30,10,55,20]

print("The given list is ",l)

num = int(input("Enter the element to search: "))

for key,value in enumerate(l):
    if value == num:
        print(f"The given number {num} is at position {key}")





