def is_permutation(a, b):
    return sorted(a) == sorted(b)


def count_digits(n):
    return len(str(n))


def generate_cubes(n_digits):
    counter = 1
    cubes = []
    while count_digits(counter ** 3) <= n_digits:
        if count_digits(counter ** 3) == n_digits:
            cubes.append(counter ** 3)
            counter += 1
        else:
            counter += 1
    return cubes


def count_permutations(cube, cubes):
    counter = 0
    for candidate in cubes:
        i = 1
        if is_permutation(str(cube), str(candidate)):
            counter += 1
    return counter


def solution(n):
    n_digit_cubes = generate_cubes(n)
    for cube in n_digit_cubes:
        if count_permutations(cube, n_digit_cubes) == 5:
            return cube


def run():
    for n in range(15):
        print(solution(n))
