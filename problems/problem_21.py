from math import sqrt


def get_and_sum_proper_factors(num):
    factors = [1]
    total = 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            if i not in factors:
                factors.append(i)
                total += i
            second_factor = int(num / i)
            if second_factor not in factors:
                factors.append(second_factor)
                total += second_factor
    return total


def solution():
    solution_list = []
    for i in range(10000):
        if get_and_sum_proper_factors(i) > i:
            a = get_and_sum_proper_factors(i)
            b = get_and_sum_proper_factors(a)
            if b == i:
                solution_list.append(a)
                solution_list.append(b)

    return solution_list


def run():
    print(sum(solution()))

