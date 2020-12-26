from math import factorial
import itertools


def run():
    target_list = []
    list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 1000000
    while len(list_a) > 0:
        if target % (factorial((len(list_a) - 1))) == 0:
            k = int((target / factorial((len(list_a) - 1))) - 1)
        else:
            k = int(target / factorial((len(list_a) - 1)))
        target = (target - k * factorial((len(list_a) - 1)))
        target_list.append(list_a[k])
        list_a.pop(k)
    print(target_list)

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    for p in (itertools.permutations(arr, 10)):
        count += 1
        if count == 1000000:
            print(p)

