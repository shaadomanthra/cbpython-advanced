from tkinter import *
class RegisterView:

    def main(self):
        window = Tk()

        window.title('Register App')

        name = Label(window,text="Enter Full Name:")
        name.grid(row=0,column=0)

        email = Label(window, text="Enter Email ID:")
        email.grid(row=1, column=0)

        password = Label(window, text="Enter Password:")
        password.grid(row=2, column=0)

        name_entry = Entry(window,width=20)
        name_entry.grid(row=0,column=1)

        email_entry = Entry(window, width=20)
        email_entry.grid(row=1, column=1)

        password_entry = Entry(window, width=20)
        password_entry.grid(row=2, column=1)

        register_button  = Button(window,text="Register")
        register_button.grid(row=3,column=1)

        window.mainloop()

