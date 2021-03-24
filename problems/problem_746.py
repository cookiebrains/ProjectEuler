import itertools as it
import math


def try_stuff():
    test = list(it.permutations([1, 2, 3, 4]))
    return test
    # print(math.factorial(8))
    # print(len(test))
    # print(eight_fac)
    # tmp = math.factorial(2021)
    # print(tmp)
    # print(math.factorial(8084))


def is_even(n):
    return n % 2 == 0


def is_every_other(perm):
    should_be_even = is_even(perm[0])
    should_be_odd = not should_be_even
    for i in range(2, (len(perm)), 2):
        if should_be_even and not is_even(perm[i]):
            return False
        elif should_be_odd and is_even(perm[i]):
            return False
    return True


def get_mf_perms(n):
    mf_perms = []
    for perm in it.permutations(list(range(0, n))):
        if is_every_other(perm):
            mf_perms.append(perm)

    return mf_perms


# perm example (7, 6, 5, 2, 3, 0, 1, 4)
# def has_family_members_sitting_together(perm):
#     for person in perm:
#
#     return False

def count_mw_perms(n):
    return n * (math.factorial(int(n / 2))) * math.factorial(int(n / 2) - 1)


# n = num families
def get_solution(n):
    total_mw_perms = count_mw_perms(4 * n)
    families_together = 8 * n * count_mw_perms(4 * n - 4) * n

    families_not_together = total_mw_perms - families_together
    return families_not_together


def run():
    print(145920 / (19 * 24 * 8 * 8 * 5))
    print(19 * 8 * 8 * 5)
    print(count_mw_perms(6))
    # print(get_solution(3))
