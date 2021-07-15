import unittest

from discount.types.BuyXGetDiscount import BuyXGetDiscount

from products.Water import Water
from products.Pepsi import Pepsi
from products.Cola import Cola

class TestGetXGetDiscount(unittest.TestCase):
    def test_sample_one(self):
        mock_rules_arguments = {
            'count': 3,
            'discount_percentage': 20
        }
        mock_count_of_products = 5
        mock_product = Pepsi

        result = BuyXGetDiscount().apply(mock_rules_arguments, mock_count_of_products, mock_product)

        self.assertEqual(result, 8)

    def test_sample_two(self):
        mock_rules_arguments = {
            'count': 3,
            'discount_percentage': 50
        }
        mock_count_of_products = 20
        mock_product = Cola

        result = BuyXGetDiscount().apply(mock_rules_arguments, mock_count_of_products, mock_product)

        self.assertEqual(result, 15)

    def test_sample_three(self):
        mock_rules_arguments = {
            'count': 3,
            'discount_percentage': 35
        }
        mock_count_of_products = 40
        mock_product = Water

        result = BuyXGetDiscount().apply(mock_rules_arguments, mock_count_of_products, mock_product)

        self.assertEqual(result, 22.1)


if __name__ == '__main__':
    unittest.main()
