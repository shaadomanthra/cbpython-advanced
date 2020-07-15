# Write python program to find the largest number in a list of numbers

def findLargest(l):
    max = l[0]

    for i in l:
        if i > max:
            max = i
    return max

l = [4,5,10,20,45,33,26,11]

# print(findLargest(l))

# print(max(l))
print(l)
l.sort()
print(l[-1])
