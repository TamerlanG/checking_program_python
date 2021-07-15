import unittest

from discount.types.BuyXGetXFree import BuyXGetXFree

class TestCalculateFreeItemsCount(unittest.TestCase):

    def test_calculate_free_items_count_sample_one(self):
        free_items_count = BuyXGetXFree().calculate_free_items_count(5, 1, 1)

        self.assertEqual(free_items_count, 2)

    def test_calculate_free_items_count_sample_two(self):
        free_items_count = BuyXGetXFree().calculate_free_items_count(6, 1, 1)

        self.assertEqual(free_items_count, 3)

    def test_calculate_free_items_count_sample_three(self):
        free_items_count = BuyXGetXFree().calculate_free_items_count(7, 1, 1)

        self.assertEqual(free_items_count, 3)

    def test_calculate_free_items_count_sample_four(self):
        free_items_count = BuyXGetXFree().calculate_free_items_count(5, 2, 1)

        self.assertEqual(free_items_count, 1)

    def test_calculate_free_items_sample_five(self):
        free_items_count = BuyXGetXFree().calculate_free_items_count(6, 2, 1)

        self.assertEqual(free_items_count, 2)

    def test_calculate_free_items_sample_six(self):
        free_items_count = BuyXGetXFree().calculate_free_items_count(5, 3, 1)

        self.assertEqual(free_items_count, 1)

if __name__ == '__main__':
    unittest.main()
