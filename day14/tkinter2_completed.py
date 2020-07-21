from tkinter import *

# add functionality
def buttonPress():
    label.config(text="Hello")

root = Tk()
# add a text label
label = Label(root,text="Welcome")
label.pack()

# add a button
button = Button(root,text="Click Me",command = buttonPress)
button.pack()

