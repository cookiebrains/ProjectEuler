def root_two():
    a, b = 0, 1
    while True:
        numerator = 2 * b + a + b
        denominator = 2 * b + a
        yield numerator, denominator
        a = b
        b = denominator


def find_solution():
    counter = 0
    solution = 0
    for x, y in root_two():
        if len(str(x)) > len(str(y)):
            solution += 1
        counter += 1
        if counter > 1000:
            break
    return solution


def run():
    print(find_solution())
