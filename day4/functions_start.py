# # # Functions in Python
#
#
# # function with varaible arguments
# def summation(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n
#     return sum
#
#
# result = summation(10, 30, 50)
# print(f"The summation is {result}")
#
# # write a function to multiple n numbers
# def multiplication(*args):
#     m = 1
#     for i in args:
#         m = m*i
#     return m
#
# result = multiplication(10,20,30)
# print(f"The multiplication is {result}")

# global & local variables

# Any value defined outside function is a global value, which can be used
# across the file
a = 10
print(a)

def sample():
    # varaibles inside functions are local variables whose data is only
    # available inside the function, and any changes made to that varaible is
    # restricted to only that function.
    global a
    a = 20
    print(a)

sample()
print(a)
