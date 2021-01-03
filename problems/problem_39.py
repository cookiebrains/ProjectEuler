def is_pythagorean_triple(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def get_triple_candidates(num):
    candidates = []
    for i in range(1, int(num / 2)):
        for j in range(1, int(num / 2) - 1):
            k = num - j - i
            if j < i and k < i:
                candidates.append((k, j, i))
    return candidates


def check_candidates(num):
    triples = []
    counter = 0
    for item in get_triple_candidates(num):
        x, y, z = item
        if is_pythagorean_triple(x, y, z):
            triples.append(item)
            counter += 1
    return counter


def solution():
    counter = 0
    value = 0
    for num in range(1, 1001):
        if check_candidates(num) > counter:
            counter = check_candidates(num)
            value = num
    return value


def run():
    print(solution())
