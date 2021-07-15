# For validators should definitely have some interface, to force the implementation of
# validate function, but unfortunately python does not support it.
from products import products_list


class ValidateProductCodes:

    def validate(self, codes):
        for code, val in codes.items():
            if not self.code_in_products(code):
                raise Exception(f"Product with code: {code} does not exist")

    def code_in_products(self, code):
        for product_code in products_list:
            if code == product_code:
                return True

        return False
