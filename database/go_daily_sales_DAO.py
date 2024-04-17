from database.DB_connect import DBConnect
from model.vendite import Vendite as v

class gds_DAO:
    @staticmethod
    def get_anni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connesione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT YEAR(Date)
               from go_daily_sales"""
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_vendite():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connesione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                       from go_daily_sales"""
            cursor.execute(query)
            for row in cursor:
                result.append(v(row["Retailer_code"],
                                row["Product_number"],
                                row["Order_method_code"],
                                row["Date"].strftime("%Y-%m-%d"),
                                row["Quantity"],
                                float(row["Unit_price"]),
                                float(row["Unit_sale_price"])))
            cursor.close()
            cnx.close()
            return result
