from console.serializers.codes_to_products import codes_to_products
from console.serializers.split_to_codes import split_to_code
from console.validators.validate_product_codes import ValidateProductCodes


class CheckOutInput:
    # TODO: Maybe do the same for serializers (input and output)
    validators = [ValidateProductCodes()]

    def get_input(self):
        user_input = input()
        serialised_input = split_to_code(user_input)

        for validator in self.validators:
            validator.validate(serialised_input)

        serialised_output = codes_to_products(serialised_input)

        return serialised_output





