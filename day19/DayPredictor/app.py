from views.YearView import YearView
class MyApp:

    def start(self):
        yv = YearView()
        yv.main()

        print("Hello")

app = MyApp()
app.start()