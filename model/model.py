from database.go_daily_sales_DAO import gds_DAO as gds
from database.go_product_DAO import gp_DAO as gp
from database.go_retailers_DAO import gr_DAO as gr


class Model:
    def __init__(self):
        self.anni = gds.get_anni()
        self.brand = gp.get_brand()
        self.retailers = gr.get_retailers()
        self.vendite = gds.get_vendite()
        self.product = gp.get_product()
