# Returns totient of all numbers smaller than or equal to n.
def all_totient_values(n):
    totient_list = [1] * (n + 2)
    for m in range(2, n + 1):
        # if not a prime, skip
        if totient_list[m] != 1:
            continue

        # multiply all multiples of m by m-1
        multiplier = m - 1
        i = m
        while i <= n:
            totient_list[i] *= multiplier
            i += m

        # multiply all multiples of higher powers by m
        v = m
        multiplier = m
        while True:
            v *= m
            if v > n:
                break
            i = v
            while i <= n:
                totient_list[i] *= multiplier
                i += v
    return totient_list


def is_permutation(a, b):
    return sorted([d for d in str(a)]) == sorted([d for d in str(b)])


def solution():
    ratio = 2
    answer = 0
    totient_values = all_totient_values(10000000)
    for i in range(2, 10000000):
        if is_permutation(i, totient_values[i]) and i / totient_values[i] < ratio:
            ratio = i / totient_values[i]
            answer = i

    return answer


def run():
    print(solution())
