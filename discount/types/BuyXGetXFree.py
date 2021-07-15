import math


class BuyXGetXFree:

    def apply(self, rules_arguments, count_of_products, product):
        count_to_buy = rules_arguments['count_to_buy']
        count_to_get_free = rules_arguments['count_to_get_free']
        price_of_single_product = product.price

        # Base Case
        if count_to_buy > count_of_products:
            return price_of_single_product * count_of_products

        # Applicable Case
        free_items_count = self.calculate_free_items_count(count_of_products, count_to_buy, count_to_get_free)
        paid_items_count = count_of_products - free_items_count

        return paid_items_count * price_of_single_product

    # TODO: FIX THIS FORMULA, RIGHT NOW IT ONLY WORKS FOR BUY (1,2) GET 1 FREE
    def calculate_free_items_count(self, count_of_products, count_to_buy, count_get_for_free):
        if count_get_for_free == 1:
            count_get_for_free += 1

        result = math.floor(count_of_products / count_get_for_free)

        if count_to_buy >= 2:
            result -= 1

        return result

