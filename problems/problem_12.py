import sys

from utilz import factor_utils


def get_triangle_number(n):
    return n * (n + 1) / 2


def get_triangle_number_with_over_500_factors():
    n = 1
    while True:
        triangle_num = get_triangle_number(n)
        message = f'Trying n = {n} and triangle number = {triangle_num}...'
        sys.stdout.write(f'\r{message}')
        if len(factor_utils.get_factors(triangle_num)) > 500:
            return n
        n += 1
        sys.stdout.flush()


def run():
    nth_triangle_num = get_triangle_number_with_over_500_factors()
    print(f'\nanswer: {nth_triangle_num}')
