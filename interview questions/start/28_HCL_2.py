# Write a program to return a sorted array (descending) from two unsorted array

a = [2,5,20,3,11]
b = [8,1,6]

c = a + b
# Method 1
c.sort(reverse=True)
print(c)

# Method 2
print(c[::-1])