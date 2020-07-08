## Lists - mutable

# basic List
l = [45,56,30,23,46,34,78,33,10,11]

#print full list
print(l)


# changing values
l[1] = 100
print(l)

# adding elements at the end
l.append(200)
print(l)

# add element at a location
l.insert(2,300)
print(l)
# remove element
l.remove(46)
print(l)

# search for an element
print(l.index(34))


# generate list with range function
r = list(range(10))
print(r)

r = list(range(5,10))
print(r)

r = list(range(2,20,3))
print(r)

## tuples - immutable
t = (10,20,30)
print(t)
print(type(t))
print(t[0])
t[0] = 1000
print(t[0])

