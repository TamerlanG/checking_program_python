import unittest

from checkout.checkout_calculator import CheckOutCalculator
from products.Water import Water
from products.Pepsi import Pepsi
from products.Cola import Cola

class TestCheckoutCalculator(unittest.TestCase):
    def test_sample_one(self):
        mock_input = {
            'CC': {
                'count': 1,
                'model': Cola
            },
            'PC': {
                'count': 1,
                'model': Pepsi
            },
            'WA': {
                'count': 1,
                'model': Water
            }
        }

        result = CheckOutCalculator().calculate(mock_input)

        self.assertEqual(result, 4.35)

    def test_sample_three(self):
        mock_input = {
            'CC': {
                'count': 2,
                'model': Cola
            },
            'PC': {
                'count': 3,
                'model': Pepsi
            },
            'WA': {
                'count': 1,
                'model': Water
            }
        }

        result = CheckOutCalculator().calculate(mock_input)

        self.assertEqual(result, 7.15)




if __name__ == '__main__':
    unittest.main()
