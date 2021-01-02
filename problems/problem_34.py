from math import factorial


def sum_digit_factorials(n):
    digits = []
    num = n
    while num > 0:
        if num % 10 != 0:
            digits.append(num % 10)
            num = int((num - num % 10) / 10)
        else:
            digits.append(0)
            num = num / 10
    return digits


def is_equal_to_factorial_sums(num):
    total = 0
    for digit in sum_digit_factorials(num):
        total += factorial(digit)
    if total == num:
        return num


def solution():
    solutions = []
    for num in range(3300000):
        if is_equal_to_factorial_sums(num) is not None:
            solutions.append(num)
    return solutions


def run():
    print(solution())

