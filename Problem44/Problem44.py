import itertools


def getPentagonal(n):
    p = (n * (3 * n - 1)) / 2
    return p


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:  # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:  # these two are the actual lines
                break  # you're looking for
            lower = x
        elif target < val:
            upper = x


def isPentagonal(maybe_pent, all_pents):
    result = binary_search(all_pents, maybe_pent)
    if result is not None:
        return True
    return False


def getPentagonals(upper_lim):
    pent_list = []
    n = 1
    for n in range(1, upper_lim):
        pent_list.append(getPentagonal(n))
    return pent_list


# doWork
# for pairs
# get sum and check list
# get difference and check list
# if sum and difference are pentagonal return pair
def doWork():
    pents = getPentagonals(5000)
    for x, y in itertools.combinations(pents, 2):
        the_sum = (x + y)
        the_dif = abs(x - y)
        if the_sum in pents and the_dif in pents:
            return x, y
        # if isPentagonal(the_sum, pents) and isPentagonal(the_dif, pents):
        #     return x - y


def testShit():
    pents = getPentagonals(72)
    for i in range(1, len(pents)):
        is_pent_for_sure = i in pents
        # print(f'{i} is_pent_for_sure: {is_pent_for_sure}')
        is_maybe_pent = isPentagonal(i, pents)
        # print(f'{i} is_maybe_pent: {is_maybe_pent}')
        # print(' ')
        if is_pent_for_sure and not is_maybe_pent:
            print(f'wrong for {i}')


print(doWork())
# testShit()
