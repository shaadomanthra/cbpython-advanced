from tkinter import *
from tkinter import messagebox
class YearView:

    def main(self):

        window = Tk()
        window.title('Year App')

        l = Label(window,text="Enter the year")
        l.grid(row=0,column=0)

        e = Entry(window,width=10)
        e.grid(row=0,column=1)

        b = Button(window,text="Submit",command=lambda:self.checkLeapYear(e.get()))
        b.grid(row=1,column=1)

        window.mainloop()

    def checkLeapYear(self,year):

       msg = f'Yes Leap Year - {year}'
       messagebox.showinfo('Check',msg)




