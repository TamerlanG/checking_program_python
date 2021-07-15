from checkout.checkout_calculator import CheckOutCalculator
from console.inputs.checkout_input import CheckOutInput
from console.outputs.checkout_output import CheckOutOutput


def run_world():
    user_input = CheckOutInput().get_input()
    total = CheckOutCalculator().calculate(user_input)
    CheckOutOutput().print_check(total)


if __name__ == '__main__':
    run_world()
