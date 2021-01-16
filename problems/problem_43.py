def three_digit_multiples(number):
    multiples = []
    for i in range(0, 1000):
        if i % number == 0:
            multiples.append(i)
    return multiples


def non_repeating_three_digit_multiples(n):
    with_repeats = three_digit_multiples(n)
    non_repeating = eliminate_repeating_digits(with_repeats, 3)
    return non_repeating


def eliminate_repeating_digits(list_of_nums):
    candidates = []
    for number in list_of_nums:
        digits = list(str(number))
        candidate = []
        for digit in digits:
            if digit not in candidate:
                candidate.append(digit)
            if len(candidate) == len(digits):
                candidates.append(candidate)
    return list(map(lambda s: int(''.join(s)), candidates))


def final_four_digits(thirteens, seventeens):
    final_four = []
    for a in thirteens:
        for b in seventeens:
            if a % 100 == (int(b / 10)):
                final_four.append(int(a / 100) * 1000 + b)
    return final_four


def final_five_digits(elevens, four_digits):
    final_five = []
    for a in elevens:
        for b in four_digits:
            if a % 100 == int(b / 100):
                final_five.append(int(a / 100) * 10000 + b)
    return final_five


def new_list_from_two(multiples, growing_list, n):
    new_list = []
    for a in multiples:
        for b in growing_list:
            if a % 100 == int(b / 10 ** n):
                new_list.append(int(a / 100) * 100 * (10 ** n) + b)
    return new_list


def run():
    # counter = 1
    # updating_list = non_repeating_three_digit_multiples(17)
    # for multiple in [13, 11, 7, 5, 3, 2]:
    #     updating_list = new_list_from_two(non_repeating_three_digit_multiples(multiple), updating_list, counter)
    #     updating_list = eliminate_repeating_digits(updating_list, counter + 3)
    #     counter += 1
    #     print(updating_list)

    three_digit_multiples_of_17 = three_digit_multiples(17)
    print(three_digit_multiples_of_17)
    b = three_digit_multiples(13)
    print(b)
    c = final_four_digits(b, three_digit_multiples_of_17)
    c = eliminate_repeating_digits(c)
    print(c)

    d = three_digit_multiples(11)
    e = final_five_digits(d, c)
    e = eliminate_repeating_digits(e)
    print(f'final five: {e}')
    f = new_list_from_two(d, c, 2)
    f = eliminate_repeating_digits(f)
    print(f'final five: {f}')
    g = three_digit_multiples(7)
    h = new_list_from_two(g, f, 3)
    h = eliminate_repeating_digits(h)
    print(f'final six: {h}')
    j = three_digit_multiples(5)
    k = new_list_from_two(j, h, 4)
    k = eliminate_repeating_digits(k)
    print(f'final seven{k}')
    l = three_digit_multiples(3)
    m = new_list_from_two(l, k, 5)
    m = eliminate_repeating_digits(m)
    print(f'final eight{m}')
    n = three_digit_multiples(2)
    o = new_list_from_two(n, m, 6)
    o = eliminate_repeating_digits(o)
    print(f'final nine digits: {o}')
    p = three_digit_multiples(1)
    q = new_list_from_two(p, o, 7)
    q = eliminate_repeating_digits(q)
    print(q)
    r = three_digit_multiples(1)
    s = new_list_from_two(r, q, 8)
    s = eliminate_repeating_digits(s)
    print(s)
    #
    print(sum([1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]))

    # e = (final_five_digits(d, c))
    # print(eliminate_repeating_digits(e, 5))
