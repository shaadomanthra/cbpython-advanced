from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calculate(a,b,opr):
    if opr == 'add':
        result= a+b
    elif opr == 'subtract':
        result= a-b
    else:
        result= a*b
    print("The result is ",result)
    messagebox.showinfo('Result','The result is '+str(result))


def main():
    window = Tk()
    window.geometry('400x400')
    window.title("Calculator App")

    a = Label(window,text="Enter a number")
    a.grid(row=0,column=0)

    a_entry = Entry(window,width=20)
    a_entry.grid(row=0,column=1)

    b = Label(window,text="Enter second number")
    b.grid(row=1,column=0)

    b_entry = Entry(window,width=20)
    b_entry.grid(row=1,column=1)

    opr = Label(window,text="Select the Operation")
    opr.grid(row=2,column=0)

    opr_entry = ttk.Combobox(window, values=["add","subtract","multiply"])
    opr_entry.grid(row=2,column=1)

    b = Button(window,text="submit",command= lambda: calculate( int(a_entry.get()),int(b_entry.get()),opr_entry.get()))
    b.grid(row=3,column=1)

    window.mainloop()

main()
