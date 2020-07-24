from views.LoginView import LoginView

class AuthApp:

    def start(self):

        lv = LoginView()
        lv.login()

app = AuthApp()
app.start()