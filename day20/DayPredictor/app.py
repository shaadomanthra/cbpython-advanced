from views.YearView import YearView
from models.YearModel import YearModel
class MyApp:

    def start(self):
        yv = YearView()
        yv.main()

app = MyApp()
app.start()
