def generate_last_three_digits():
    num = []
    for i in range(100, 1000):
        if i % 17 == 0:
            num.append(i)
    return num


def multiples_of_thirteen():
    num = []
    for i in range(100, 1000):
        if i % 13 == 0:
            num.append(i)
    return num


def get_candidates_list():
    candidates = []
    for number in range(1000, 10000):
        digits = list(str(number))
        candidate = []
        for digit in digits:
            if int(digit) != 0 and digit not in candidate:
                candidate.append(digit)
            if len(candidate) == 4:
                candidates.append(candidate)
    return list(map(lambda s: int(''.join(s)), candidates))


def eliminate_repeating_digits(list_of_nums):
    candidates = []
    for number in list_of_nums:
        digits = list(str(number))
        candidate = []
        for digit in digits:
            if digit not in candidate:
                candidate.append(digit)
            if len(candidate) == len(digit):
                candidates.append(candidate)
    return list(map(lambda s: int(''.join(s)), candidates))


def final_four_digits(thirteens, seventeens):
    final_four = []
    for a in thirteens:
        for b in seventeens:
            if a % 100 == (int(b/10)):
                final_four.append(int(a/100) * 1000 + b)
    return final_four


def run():
    a = generate_last_three_digits()
    b = multiples_of_thirteen()
    c = final_four_digits(b, a)

