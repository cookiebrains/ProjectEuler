from math import sqrt


def get_and_sum_proper_divisors(num):
    factors = [1]
    total = 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            total += i
            second_factor = int(num / i)
            factors.append(second_factor)
            total += second_factor
    return total


def solution():
    solution_list = []
    for i in range(10000):
        if get_and_sum_proper_divisors(i) > i:
            a = get_and_sum_proper_divisors(i)
            b = get_and_sum_proper_divisors(a)
            if b == i:
                solution_list.append(a)
                solution_list.append(b)

    return solution_list


def run():
    print(sum(solution()))

