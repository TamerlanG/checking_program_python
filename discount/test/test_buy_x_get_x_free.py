import unittest

from discount.types.BuyXGetXFree import BuyXGetXFree
from products.Water import Water
from products.Pepsi import Pepsi
from products.Cola import Cola


class TestBuyXGetXFree(unittest.TestCase):
    def test_sample_one(self):
        mock_rules_arguments = {
            'count_to_buy': 1,
            'count_to_get_free': 1
        }
        mock_count_of_products = 5
        mock_product = Cola

        result = BuyXGetXFree().apply(mock_rules_arguments, mock_count_of_products, mock_product)

        self.assertEqual(result, 4.5)

    def test_sample_two(self):
        mock_rules_arguments = {
            'count_to_buy': 1,
            'count_to_get_free': 1
        }
        mock_count_of_products = 6
        mock_product = Pepsi

        result = BuyXGetXFree().apply(mock_rules_arguments, mock_count_of_products, mock_product)

        self.assertEqual(result, 6)

    def test_sample_three(self):
        mock_rules_arguments = {
            'count_to_buy': 1,
            'count_to_get_free': 1
        }
        mock_count_of_products = 10
        mock_product = Water

        result = BuyXGetXFree().apply(mock_rules_arguments, mock_count_of_products, mock_product)

        self.assertEqual(result, 4.25)

if __name__ == '__main__':
    unittest.main()
