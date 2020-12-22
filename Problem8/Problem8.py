def get_the_huge_number():
    open_file = open("big_num.txt", "r")
    number = open_file.read().replace("\n", "")
    open_file.close()
    return number


def get_list_of_digits(num):
    digits = []
    for i in num:
        digits.append(i)
    return digits


def multiply_adjacent_nums(digits, range_pair):
    product = 1
    m, n = range_pair
    for digit in digits[m:n]:
        product *= int(digit)
    return product


def generate_index_pairs(lower_lim, upper_lim, span):
    pairs = [(x, x + span)
             for x in range(lower_lim, upper_lim)
             ]
    return pairs


print(generate_index_pairs(0, 87, 13))


def do_work():
    highest_prod = 0
    a = get_the_huge_number()
    digits = get_list_of_digits(a)
    for pair in generate_index_pairs(0, 988, 13):
        if multiply_adjacent_nums(digits, pair) > highest_prod:
            highest_prod = multiply_adjacent_nums(digits, pair)
    print(highest_prod)


do_work()
