# # Functions in Python

# function with varaible arguments
def var_args_func(*args):
	s = 0;
	for a in args:
		s = s + a
	return s
# print(var_args_func(4,2,4,5))
# print(var_args_func(4,2,4,5,10))

# global & local variables
a = 10
print(a)

def func():
	global a
	a=12
	print(a)

func()

print(a)
