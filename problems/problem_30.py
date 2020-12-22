def SumOfDigitsToFifthPower(n):
    result = 0
    for dig in str(n):
        result += (int(dig))**5
    return result


def run():
    total = 0
    for i in range(2, 1000000):
        if SumOfDigitsToFifthPower(i) == i:
            total += i
    print(total)
