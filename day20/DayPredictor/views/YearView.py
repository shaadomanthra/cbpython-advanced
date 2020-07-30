from tkinter import *
from tkinter import messagebox
from models.YearModel import YearModel
from controllers.YearController import YearController

class YearView:

    def main(self):

        window = Tk()
        window.title('Year App')

        l = Label(window,text="Enter the year")
        l.grid(row=0,column=0)

        e = Entry(window,width=10)
        e.grid(row=0,column=1)

        b = Button(window,text="Submit",command=lambda:self.checkLeapYear(int(e.get())))
        b.grid(row=1,column=1)

        window.mainloop()

    def checkLeapYear(self,year):

        yc  =YearController()
        leap = yc.checkLeap(year)

        ym = YearModel()
        ym.insert(year,leap)
        if leap:
            msg = f'Yes Leap Year - {year}'
            messagebox.showinfo('Check',msg)
        else:
            msg = f'No, Not a Leap Year - {year}'
            messagebox.showinfo('Check', msg)





