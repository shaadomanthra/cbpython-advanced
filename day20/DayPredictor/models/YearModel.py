from models.db import *

class YearModel:

    def insert(self,year,leap):
        conn = connect('year.db')
        query = f"INSERT INTO leapyear (year,leap) VALUES({year},{leap})"
        execute(conn,query)
        print("One record inserted")

