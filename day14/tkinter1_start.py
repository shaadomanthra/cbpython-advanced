# import tkinter
from tkinter import *

# create a window
root = Tk()

# add a text label
l1 = Label(root, text = "Welcome to the class")
l1.grid(row=0,column=0)

# add a button
b1 = Button(root, text= "Hurray!")
b1.grid(row=0,column=1)

root.mainloop()


