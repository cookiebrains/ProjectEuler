def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def find_solution():
    i = 1
    for n in fibonacci():
        if len(str(n)) > 999:
            return i
        i += 1


def run():
    print(find_solution())
