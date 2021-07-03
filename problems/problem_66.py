import math


def get_m(d, a, m):
    return d * a - m


def get_d(n, m, d):
    return (n - m ** 2) / d


def get_a(n, m, d):
    return int((math.sqrt(n) + m) / d)


def cont_fractions_sqrt_n(n):
    a_list = []
    m = 0
    d = 1
    a_o = int(math.sqrt(n))
    a = int(math.sqrt(n))

    while True:
        if a == 2 * a_o:
            a_list.append(a)
            return a_list
        a_list.append(a)
        m = get_m(d, a, m)
        d = get_d(n, m, d)
        a = get_a(n, m, d)


def get_tuple(ao_list):
    n = ao_list.pop()
    m = ao_list.pop()
    numerator = 1
    while True:

        if len(ao_list) == 0:

            return m * n + numerator, n
        else:
            numerator, n = n, n * m + numerator
            m = ao_list.pop()


def get_diophantine_term1(num):
    ao_list = cont_fractions_sqrt_n(num)
    i = 2
    while True:
        while i <= len(ao_list):
            x, y = get_tuple(ao_list[:i])
            if x ** 2 - num * y ** 2 == 1:
                return x
            else:
                i += 1
        ao_list = ao_list + ao_list[1:]


def solution():
    biggest_diophantine_term1 = 0
    answer_n = 0

    for n in range(2, 1001):
        if int(math.sqrt(n) + 0.5) ** 2 == n:
            continue
        else:
            term1 = get_diophantine_term1(n)
            if term1 > biggest_diophantine_term1:
                biggest_diophantine_term1 = term1
                answer_n = n

    return answer_n


def run():
    print(solution())
