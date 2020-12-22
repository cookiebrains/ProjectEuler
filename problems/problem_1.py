def MakeMultiplesSet(n, m, upper_lim):
    multiples = set()
    i = 1
    j = 1
    while (n * i) < upper_lim:
        multiples.add(n * i)
        i += 1
    while (m * j) < upper_lim:
        multiples.add(m * j)
        j += 1
    return multiples


def SumNumsInSet(n):
    total = 0
    for i in n:
        total += i
    return total


def run():
    print(SumNumsInSet(MakeMultiplesSet(3, 5, 1000)))
