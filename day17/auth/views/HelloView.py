from tkinter import *
from views.LoginView import LoginView
from views.RegisterView import RegisterView

class HelloView:

    def main(self):
        window = Tk()

        window.title('Hello App')
        window.geometry('300x300')

        l = Label(window,text="hello")
        l.pack()

        lobj = LoginView()

        b = Button(window,text="login",command=lobj.main)
        b.pack()

        robj = RegisterView()
        b2 = Button(window, text="register", command =robj.main)
        b2.pack()

        window.mainloop()