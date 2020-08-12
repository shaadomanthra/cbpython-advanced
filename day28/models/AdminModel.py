from models.db import *

class AdminModel:

    def getAllRecords(self):
        conn = connect("app.db")
        query = "SELECT * from barcodes"
        results = fetchall(conn,query)
        return results


