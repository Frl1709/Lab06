import datetime
from dataclasses import dataclass

@dataclass
class Vendite:
    retailer_code: int
    product_number: int
    order_method_code: int
    date: datetime.date
    quantity: str
    unit_price: float
    unit_sale_price: float



    def __eq__(self, other):
        return self.retailer_code == other

    def __hash__(self):
        return hash((self.retailer_code, self.product_number, self.order_method_code, self))
