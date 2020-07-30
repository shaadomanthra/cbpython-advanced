from views.YearView import YearView
from models.YearModel import YearModel
class MyApp:

    def start(self):
        yv = YearView()
        yv.main()

        print("Hello")

    # def insert(self,year,leap):
    #     ym = YearModel()
    #     ym.insert(year,leap)

app = MyApp()
app.start()
