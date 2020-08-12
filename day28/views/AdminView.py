from tkinter import *
from models.AdminModel import AdminModel
class AdminView:

    def main(self):

        window = Tk()

        am = AdminModel()
        result = am.getAllRecords()

        msg = ''
        for i in result:
            line = str(i[2]) + ' - ' + str(i[1])
            msg = msg + line + "\n"

        label = Label(window,text=msg,padx=30,pady=30)
        label.pack()

        window.mainloop()

