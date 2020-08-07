from views.BarView import BarView
from models.BarModel import BarModel

class MyApp:

    def start(self):
        print("Application started")

        bv = BarView()
        bv.main()

    def db(self):
        bm = BarModel()
        # bm.insertBarcode("Another Text","Ramesh")
        result = bm.fetch("Another Text","Ramesh")
        print(result)


app = MyApp()
app.db()