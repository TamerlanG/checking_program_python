from discount.rules import Rules


class DiscountManager:
    rules = Rules().rules

    def apply_discount(self, serialized_input):
        keys_to_exclude = {'product', 'type'}
        prices = []

        for product_code, details in serialized_input.items():
            rule_found = False

            # Use Discounted Price
            for rule in self.rules:
                if rule['product'].code == product_code:
                    rule_found = True
                    price = rule['type']().apply(self.exclude_keys(keys_to_exclude, rule), details['count'], details['model'])
                    prices.append(price)
                    continue

            # Use Normal Price
            if not rule_found:
                price = details['count'] * details['model'].price
                prices.append(price)

        return prices

    # Return new dictionary excluding given keys
    def exclude_keys(self, keys, dict):
        return {k: v for k, v in dict.items() if k not in keys}