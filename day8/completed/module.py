## Program to understand modules

# import module and invoke function
import hello
hello.hello_basic()

# import with a name
import hello as h
h.hello_basic()

# import all function
from hello import *
hello_name('Teja')

# import specific functions
from hello import hello_basic
hello_in_french()

