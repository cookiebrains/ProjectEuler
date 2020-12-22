def add_digits(n):
    sum_of_digits = 0
    for item in str(n):
        sum_of_digits += int(item)
    return sum_of_digits


def run():
    print(add_digits(2**1000))
