from products import products_list


def codes_to_products(serialized_input):
    results = {}

    for code, count in serialized_input.items():
        for product_code, model in products_list.items():
            if code == product_code:
                results[code] = {
                    'count': count,
                    'model': model
                }
    return results
