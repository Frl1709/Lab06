from database.DB_connect import DBConnect
from model.product import Product as p


class gp_DAO:

    @staticmethod
    def get_brand():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connesione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT DISTINCT Product_brand
                       from go_products"""
            cursor.execute(query)
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_product():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connesione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                           from go_products"""
            cursor.execute(query)
            for row in cursor:
                result.append(p(row["Product_number"],
                                row["Product_line"],
                                row["Product_type"],
                                row["Product"],
                                row["Product_brand"],
                                row["Product_color"],
                                row["Unit_cost"],
                                row["Unit_price"]))
            cursor.close()
            cnx.close()
            return result
