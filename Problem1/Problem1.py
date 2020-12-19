def MakeMultiplesSet(n, m, upper_lim):
    multiples = set()
    for anynum in range(1, 1000000):
        if n * anynum < upper_lim:
            multiples.add(n * anynum)
        if m * anynum < upper_lim:
            multiples.add(m * anynum)
    return multiples


def SumNumsInSet(n):
    total = 0
    for i in n:
        total += i
    return total


def DoWork():
    print(SumNumsInSet(MakeMultiplesSet(3, 5, 1000)))


DoWork()
