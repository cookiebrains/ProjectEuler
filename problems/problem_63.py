def count_digits(n):
    return len(str(n))


def count_n_digit_powers(num):
    n_digit_powers = []
    for i in range(30):
        if count_digits(num ** i) == i:
            n_digit_powers.append(num ** i)
    return len(n_digit_powers)


def solution():
    total_n_digit_powers = 0
    for num in range(1, 10):
        total_n_digit_powers += count_n_digit_powers(num)
    return total_n_digit_powers


def run():
    print(solution())
