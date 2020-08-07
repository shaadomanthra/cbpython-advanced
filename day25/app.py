from views.BarView import BarView
from models.BarModel import BarModel

class MyApp:

    def start(self):
        print("Application started")

        bv = BarView()
        bv.main()

    def db(self):
        bm = BarModel()
        bm.insertBarcode("This is sample text","Krishna Teja")


app = MyApp()
app.db()