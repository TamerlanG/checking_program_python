from discount.discount_manager import DiscountManager


class CheckOutCalculator:

    def calculate(self, serialized_input):
        discounted_prices = DiscountManager().apply_discount(serialized_input)
        total = 0

        for price in discounted_prices:
            total += price

        return total
