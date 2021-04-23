# circle radius 2
def all_possible_p2(a, b):
    p2 = []

    if a > b:
        for d in range(-1, (a * (-1) - 1), -1):
            for c in range((d * a - 1), a + 1):
                p2.append((c, d))

    if a == b:
        for d in range(-1, (a * (-1) - 1), -1):
            for c in range(d + 1, a + 1):
                p2.append((c, d))
    return p2


def run():
    print((all_possible_p2(2, 1)))
