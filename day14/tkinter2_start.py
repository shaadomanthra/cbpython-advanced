# Import tkinter
from tkinter import *

# add functionality
def changeText():
    l.config(text="The updated text")

root =  Tk()
# add a text label
l = Label(root, text = "Welcome")
l.pack()

# add a button
b = Button(root, text="Click Me", command=changeText)
b.pack()

root.mainloop()

