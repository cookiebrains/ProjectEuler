from itertools import permutations


def run():
    divisors = [2, 3, 5, 7, 11, 13, 17]
    results = []
    for i in permutations('0123456789'):
        number = ''.join(i)
        if number[0] != '0':
            j = 0
            for divisor in divisors:
                j += 1
                numerator = number[j] + number[j + 1] + number[j + 2]
                if int(numerator) % divisor != 0:
                    break
            else:
                results.append(int(number))
    print(sum(results))
