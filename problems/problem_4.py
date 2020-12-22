import itertools


def create_list(r1, r2):
    return list(range(r1, r2 + 1))


def reversal(a):
    return a[::-1]


def generate_solution():
    for x, y in itertools.combinations((create_list(100, 999)), 2):
        if str(x * y) == reversal(str(x * y)):
            yield x, y, x*y


def run():
    for i in generate_solution():
        print(i)


def another_borrowed_solution():
    maxp = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            p = i * j
            if str(p) == str(p)[::-1] and p > maxp:
                maxp = p

    print(maxp)
