import math


def get_m(d, a, m):
    return d * a - m


def get_d(n, m, d):
    return (n - m ** 2) / d


def get_a(n, m, d):
    return int((math.sqrt(n) + m) / d)


def period_sqrt_n(n):
    a_list = []
    m = 0
    d = 1
    a_o = int(math.sqrt(n))
    a = int(math.sqrt(n))

    while True:
        if a == 2 * a_o:
            return len(a_list)
        a_list.append(a)
        m = get_m(d, a, m)
        d = get_d(n, m, d)
        a = get_a(n, m, d)


def solution():
    odd_periods = 0
    for n in range(2, 10001):
        if int(math.sqrt(n) + 0.5) ** 2 == n:
            continue
        else:
            if period_sqrt_n(n) % 2 == 1:
                odd_periods += 1
    return odd_periods


def run():
    print(solution())
