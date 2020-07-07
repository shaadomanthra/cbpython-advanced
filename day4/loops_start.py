# # Working with loops
# a = 10
# # define a while loop
# while(a<20):
#     print(a)
#     a = a+1

# define a for loop
# for i in range(5):
#     print(i)

# use the break and continue statements
for i in range(20):
    if i == 10:
        break
    print(i)

for i in range(20):
    if i%2 == 0:
        continue
    print(i)

# use a for loop over a collection
days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
for d in days:
    print(d)

#using the enumerate() function to get index
for key,value in enumerate(days):
    print(key,value)
