from tkinter import *
from tkinter import messagebox
from models.LoginModel import LoginModel
class LoginView:

    def main(self):
        window = Tk()

        window.title('Login App')

        email = Label(window, text="Enter Email ID:")
        email.grid(row=1, column=0)

        password = Label(window, text="Enter Password:")
        password.grid(row=2, column=0)


        email_entry = Entry(window, width=20)
        email_entry.grid(row=1, column=1)

        password_entry = Entry(window, width=20)
        password_entry.grid(row=2, column=1)

        login_button = Button(window, text="Login",command=lambda: self.checkUser(email_entry.get(),password_entry.get()))
        login_button.grid(row=3, column=1)

        window.mainloop()

    def checkUser(self,email,password):

        lm = LoginModel()
        result = lm.getUser(email,password)
        if result:
            messagebox.showinfo('Success','User found')
        else:
            messagebox.showerror('Error', 'Invalid Credentials')


