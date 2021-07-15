def split_to_code(user_input):
    codes = user_input.split()
    result = {}

    for code in codes:
        if code in result:
            result[code] += 1
        else:
            result[code] = 1

    return result
