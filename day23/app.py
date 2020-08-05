from views.BarView import BarView

class MyApp:

    def start(self):
        print("Application started")

        bv = BarView()
        bv.main()


app = MyApp()
app.start()