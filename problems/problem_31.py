def get_original_dict(upper_lim):
    original_dict = {}
    for number in range(0, upper_lim):
        original_dict[number] = 1
    return original_dict


def update_dict_by_next_currency(current_dict, currency):
    for x in currency:
        for key in current_dict:
            k = key - x
            if k >= 0:
                current_dict[key] = current_dict[key] + current_dict[k]
    return current_dict


def run():
    a = get_original_dict(201)
    print(update_dict_by_next_currency(a, [2, 5, 10, 20, 50, 100, 200]))

