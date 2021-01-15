def find_mystery_num():
    for number in range(100):
        if 2 * (number + 300) == 27 * number:
            return number


def shrinking_multipliers():
    x = 10
    for i in range(10):
        result = x * (x + 1)
        print(x, result)
        x -= 1


shrinking_multipliers()
