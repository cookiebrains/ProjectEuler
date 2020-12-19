def SumOfDigitsToFifthPower(n):
    result = 0
    for num in str(n):
        result += (int(num))**5
    return result


def DoWork():
    total = 0
    for i in range(2, 10000000):
        if SumOfDigitsToFifthPower(i) == i:
            total += i
    print(total)


DoWork()

