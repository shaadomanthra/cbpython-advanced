## Day2 recap concepts

import sys

# # variables
# m = 10
# print(m)
# print(type(m))
#
# m = 'Teja'
# print(m)
#
# # getting the datatype of varaible
# print(type(m))
#
# # strings
# message = "The name given is {}".format(m)
# print(message)
#
# message = f"shortcut method - {m}"
# print(message)

# take input from commandline
# if len(sys.argv) > 1:
#     str = sys.argv[1]
#     print("The first argument is -",str)
# else:
#     print('No arguments are given')

str = sys.argv[1] if len(sys.argv) > 1 else None
print(str)
