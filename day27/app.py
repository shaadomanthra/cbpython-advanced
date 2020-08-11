from views.BarView import BarView
from views.LoginView import LoginView
from views.RegisterView import RegisterView

class MyApp:

    def start(self):
        print("Application started")

        lv = LoginView()
        lv.main()

        # bv = BarView()
        # bv.main()


app = MyApp()
app.start()