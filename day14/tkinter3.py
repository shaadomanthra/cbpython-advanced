# Import tkinter
from tkinter import *

def greeting():
    t = name_entry.get()
    message.config(text="Welcome "+t)

root =  Tk()
root.title("KT Application")
name = Label(root, text="Enter your name")
name.grid(row=0,column=0)

name_entry = Entry(root, width=10)
name_entry.grid(row=0,column = 1)

b = Button(root, text="greet",command=greeting)
b.grid(row=1,column=1)

message = Label(root, text="")
message.grid(row=2,column=1)

root.mainloop()

