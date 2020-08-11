from tkinter import *
from tkinter import messagebox
from models.LoginModel import LoginModel
class LoginView:

    def main(self):
        self.window = Tk()

        self.window.title('Login App')

        email = Label(self.window, text="Enter Email ID:")
        email.grid(row=1, column=0)

        password = Label(self.window, text="Enter Password:")
        password.grid(row=2, column=0)


        email_entry = Entry(self.window, width=20)
        email_entry.grid(row=1, column=1)

        password_entry = Entry(self.window, show="*",width=20)
        password_entry.grid(row=2, column=1)

        login_button = Button(self.window, text="Login",command=lambda: self.checkUser(email_entry.get(),password_entry.get()))
        login_button.grid(row=3, column=1)

        self.window.mainloop()

    def checkUser(self,email,password):

        lm = LoginModel()
        result = lm.getUser(email,password)
        if result:
            messagebox.showinfo('Success','User found')
            self.window.destroy()
        else:
            messagebox.showerror('Error', 'Invalid Credentials')


