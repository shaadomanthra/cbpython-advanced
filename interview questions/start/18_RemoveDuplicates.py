# Write a python program to remove duplicates in a list
l = [20,30,45,20,30,10,55,20]

print("The Given List is ",l)

temp = []
for i in l:
    if i not in temp:
        temp.append(i)

print("The list with no duplicates is",temp)

# collection - OrderedDict