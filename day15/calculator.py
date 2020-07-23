from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calculate(a,b,opr):
    if opr == 'add':
        result= a+b
    elif opr == 'subtract':
        result= a-b
    elif opr == 'division':
        if b == 0:
            messagebox.showerror('Error','The second number cannot be 0')
        else:
            result = a//b
    elif opr=='power':
        result = a**b
    else:
        result= a*b
    print("The result is ",result)
    message = f" a = {a} and b ={b} and opr ={opr}, the result is {result}"
    messagebox.showinfo('Result',message)


def main():
    window = Tk()
    window.title("Calculator App")

    frame = Frame(window,bg="white",padx=20,pady=20)
    frame.grid()

    a = Label(frame,text="Enter a number")
    a.grid(row=0,column=0)

    a_entry = Entry(frame,width=20)
    a_entry.grid(row=0,column=1,pady=10)

    b = Label(frame,text="Enter second number")
    b.grid(row=1,column=0)

    b_entry = Entry(frame,width=20)
    b_entry.grid(row=1,column=1,pady=10)

    opr = Label(frame,text="Select the Operation")
    opr.grid(row=2,column=0)

    opr_entry = ttk.Combobox(frame, values=["add","subtract","multiply","division","power"])
    opr_entry.grid(row=2,column=1,pady=10)

    b = Button(frame,text="submit",command= lambda: calculate( int(a_entry.get()),int(b_entry.get()),opr_entry.get()))
    b.grid(row=3,column=1,pady=10)

    window.mainloop()

main()
