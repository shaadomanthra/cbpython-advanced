## dictionary

d ={'name':'Teja','age':29,'address':'Hyderabad','Male':True}
# print via index
print(d['age'])
for i in d:
    print(i,d[i])

# print keys
for i in d.keys():
    print(i)
# print only values
for i in d.values():
    print(i)

# print key value pair
for key,value in d.items():
    print(key,value)

# changing values
print(d)
d['age'] = 100
print(d)
# search key
print('city' in d)

# serach value
print('Teja' in d.values())

## Sets - for unordered unique elements
a = set("123456")
b = set("239")
c = a | b
print(c)
d = a & b
print(d)
