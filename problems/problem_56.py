import random
import math


# def sum_digits(num):
#     digits = []
#     working_num = num
#     while working_num != 0:
#         digits.append(working_num % 10)
#         working_num = int((working_num - (working_num % 10)) / 10)
#     return sum(digits)
#
#
# def sum_digits_with_strings(num):
#     return sum(map(lambda digit: int(digit), [char for char in str(num)]))


# def benchmark_that_shit(use_strings=False):
#     lower_lim = 200
#     upper_lim = 400
#     for i in range(1000001):
#         num_digits = random.randint(lower_lim, upper_lim)
#         num = random.getrandbits(num_digits)
#         if use_strings:
#             sum = sum_digits_with_strings(num)
#         else:
#             sum = sum_digits(num)

def sum_digits(num):
    return sum(map(lambda digit: int(digit), [char for char in str(num)]))


def get_it():
    largest_sum = 0
    for i in range(80, 100):
        for j in range(80, 100):
            digits_sum = sum_digits(i**j)
            if digits_sum > largest_sum:
                largest_sum = digits_sum
    return largest_sum


def run():
    # benchmark_that_shit()  # 37.32s, 38.78s
    # benchmark_that_shit(use_strings=True)  # 13.47s, 13.3s
    print(get_it())
