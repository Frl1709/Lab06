from database.DB_connect import DBConnect
from model.retailer import Retailer as r


class gr_DAO:

    @staticmethod
    def get_retailers():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connesione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM go_retailers"""
            cursor.execute(query)
            for row in cursor:
                result.append(r(row["Retailer_code"],
                                row["Retailer_name"],
                                row["Type"],
                                row["Country"]))
            cursor.close()
            cnx.close()
            return result

