import unittest
from console.validators.validate_product_codes import ValidateProductCodes

class TestValidateProductCode(unittest.TestCase):

    def test_should_raise_exception_for_unknown_product_code(self):
        mock_input = {
            'WF': 3,
            'PC': 2,
            'WA': 2
        }

        with self.assertRaises(Exception):
            ValidateProductCodes().validate(mock_input)


    def test_should_pass_validation(self):
        mock_input = {
            'CC': 3,
            'PC': 2,
            'WA': 2
        }

        result = ValidateProductCodes().validate(mock_input)

        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
