from views.BarView import BarView
from views.LoginView import LoginView
from views.RegisterView import RegisterView
from views.AdminView import AdminView
class MyApp:

    def start(self):
        print("Application started")

        lv = LoginView()
        lv.main()

        if( lv.role =='admin'):
            av = AdminView()
            av.main()
        else:
            bv = BarView()
            bv.username = lv.username
            bv.main()




app = MyApp()
app.start()