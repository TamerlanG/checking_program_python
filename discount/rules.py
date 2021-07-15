from discount.types.BuyXGetXFree import BuyXGetXFree
from discount.types.BuyXGetDiscount import BuyXGetDiscount
from products.Pepsi import Pepsi
from products.Cola import Cola


class Rules:
    def __init__(self):
        self.rules = [
            {
                'product': Pepsi,
                'type': BuyXGetDiscount,
                'count': 3,
                'discount_percentage': 20,
            },
            {
                'product': Cola,
                'type': BuyXGetXFree,
                'count_to_buy': 1,
                'count_to_get_free': 1
            }
        ]
