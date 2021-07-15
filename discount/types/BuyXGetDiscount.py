class BuyXGetDiscount:

    def apply(self, rules_arguments, count_of_products, product):
        count_to_get_discount = rules_arguments['count']
        discount_percentage = rules_arguments['discount_percentage']
        price_of_single_product = product.price

        # Base Case
        if count_to_get_discount > count_of_products:
            return price_of_single_product * count_of_products

        # Applicable Case
        discount = (discount_percentage / 100) * price_of_single_product
        new_price = price_of_single_product - discount

        return new_price * count_of_products