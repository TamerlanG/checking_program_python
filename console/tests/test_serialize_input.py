import unittest

from console.serializers.split_to_codes import split_to_code


class TestSerializeInput(unittest.TestCase):

    def test_should_properly_serialize_input(self):
        mock_input = 'CC CC CC PC WA PC WA'
        mock_output = {
            'CC': 3,
            'PC': 2,
            'WA': 2
        }

        result = split_to_code(mock_input)

        self.assertEqual(result, mock_output)


if __name__ == '__main__':
    unittest.main()
