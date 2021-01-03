from utilz.prime_utils import *
import itertools


def is_pan_digital(num):
    changing_num = num
    check_set = set()
    while changing_num != 0:
        if changing_num % 10 != 0:
            check_set.add(changing_num % 10)
            changing_num = changing_num - (changing_num % 10)
            changing_num = changing_num / 10
        else:
            changing_num = changing_num / 10
    if len(check_set) == 9 == len(str(num)):
        return True
    else:
        return False


def solution():
    for i in itertools.permutations([7, 6, 5, 4, 3, 2, 1]):
        s = [str(digit) for digit in i]
        num = int(''.join(s))
        if is_prime(num):
            return num


def run():
    print(solution())

# I tried 9 and 8 digit permutations first, returned None
