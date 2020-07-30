from views.LoginView import LoginView
from views.RegisterView import RegisterView
from views.HelloView import HelloView
from models.RegisterModel import RegisterModel

class AuthApp:

    def start(self):
        l = LoginView()
        l.main()
        #
        # r = RegisterView()
        # r.main()

        # h = HelloView()
        # h.main()



app = AuthApp()
app.start()
