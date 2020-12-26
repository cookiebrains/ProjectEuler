from math import sqrt


def get_and_sum_proper_divisors(num):
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


def is_abundant(n):
    return n < get_and_sum_proper_divisors(n)


def get_abundant_numbers(upper_lim):
    abundant_numbers = []
    for num in range(1, upper_lim):
        if get_and_sum_proper_divisors(num) > num:
            abundant_numbers.append(num)
    return abundant_numbers


def run():
    abundant_numbers = []
    for n in range(2, 28124):
        if is_abundant(n):
            abundant_numbers.append(n)

    no_abundant_sums_sum = 0
    for num in range(1, 28124):
        has_abundant_sum = False
        for a in abundant_numbers:
            half = num / 2
            if a > half:
                break
            if is_abundant(num-a):
                has_abundant_sum = True
                break
        if not has_abundant_sum:
            no_abundant_sums_sum += num
    print(f'total: {no_abundant_sums_sum}')

# total: 4179871


