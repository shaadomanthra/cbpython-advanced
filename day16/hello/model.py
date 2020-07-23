from db import *

class model:

    def insert(self,name,count):
        conn = connect('app.db')



m = model()
m.insert('teja',4)