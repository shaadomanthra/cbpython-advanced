from tkinter import *
from controller import controller

class view:

    # The design
    def main(self):
        root = Tk()
        root.title('Hello App')

        l = Label(root,text='Enter your name')
        l.pack()
        e = Entry(root, width=10)
        e.pack()
        b = Button(root, text="click",command=lambda:self.greet(e.get()))
        b.pack()
        self.l2 = Label(root,text='')
        self.l2.pack()

        root.mainloop()

    def greet(self,name):

        controlObj = controller()
        count = controlObj.counter(name)

        self.l2.config(text=f"The length of {name} is {count}")




viewobj = view()
viewobj.main()

