from math import sqrt


def getPrimes():
    i = 2
    while True:
        if isPrime(i):
            yield i
        i += 1


def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def isPrimeFactor(p, num):
    if isPrime(p) and num % p == 0:
        return True


def getLowestPrimeFactor(n):
    for p in getPrimes():
        if p > n:
            return n
        if isPrimeFactor(p, n):
            return p


def primeFactorization(n):
    factorization_list = []
    running_total = n
    while True:
        current_prime_factor = getLowestPrimeFactor(running_total)
        running_total = running_total / current_prime_factor
        factorization_list.append(current_prime_factor)
        if running_total == 1:
            break
    return factorization_list


def get_candidates_list():
    candidates = []
    for number in range(1000, 10000):
        digits = list(str(number))
        candidate = []
        for digit in digits:
            if int(digit) != 0 and digit not in candidate:
                candidate.append(digit)
            if len(candidate) == 4:
                candidates.append(candidate)
    return list(map(lambda s: int(''.join(s)), candidates))


def two_prime_factor_solutions(candidates):
    solutions = []
    for each in candidates:
        if len(primeFactorization(each)) == 2:
            check_set = set()
            for digit in str(each):
                check_set.add(digit)
            for num in primeFactorization(each):
                for digit in str(num):
                    check_set.add(digit)
            print(check_set)
            if len(check_set) == 9:
                solutions.append(each)
    return solutions


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
    if len(check_set) == len(str(num)):
        return True
    else:
        return False


def check_list_of_threes(three_list):
    s = [str(i) for i in three_list]
    res = (''.join(s))
    if len(res) == 9 and is_pan_digital(int(res)):
        return three_list


def divide_and_check(number):
    list_of_threes = []
    for i in range(1, 100):
        if number % i == 0:
            q = int(number / i)
            list_of_threes.append([i, q, number])
    return list_of_threes


def solution():
    solution_list = []
    a = get_candidates_list()
    for number in a:
        b = divide_and_check(number)
        for candidate in b:
            if check_list_of_threes(candidate) is not None:
                solution_list.append(check_list_of_threes(candidate))
    return solution_list


def run():
    print(solution())

    # can't be one by one, one by two, or one by three, or two by two, as these don't have enough digits.
    # also can't be three by three, total digits = too many
    # could be one by four or two by three
    # basically we're looking at 4 digit numbers, 1001 to 9999, and from these, we only need to look at
    # numbers with no zeros and no repeated numbers
    # there are no solutions with exactly two prime factors
