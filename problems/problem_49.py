import math
import itertools


def isPrime(num):
    if num == 2:
        return True
    square_root_approximate = math.ceil(math.sqrt(num)) + 1
    is_prime = True
    for i in range(2, square_root_approximate):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


def getPrimes():
    primes = []
    for i in range(1000, 9999):
        if isPrime(i):
            primes.append(str(i))
    return primes


def getPrimePermutations(prime, all_primes):
    prime_perms = []
    prime_digits = []
    prime_digits[:] = prime
    for perm_as_digits in itertools.permutations(prime_digits):
        perm = ''.join(perm_as_digits)
        if perm in all_primes and perm not in prime_perms:
            prime_perms.append(perm)
    return prime_perms


# Return arithmetic sequence or None
def getArithmeticSequence(numbers_as_strings):
    numbers = [int(i) for i in numbers_as_strings]

    for perm in itertools.permutations(numbers, 3):
        ordered = sorted(perm, key=int, reverse=True)
        if (ordered[0] - ordered[1]) == (ordered[1] - ordered[2]):
            return sorted(perm)

    return None


def hasAnswer(answers, answer):
    for a in answers:
        if a == answer:
            return True
    return False


def findAnswer49():
    answers = []
    all_primes = getPrimes()
    for prime in all_primes:
        prime_perms = getPrimePermutations(prime, all_primes)
        if len(prime_perms) < 3:
            continue
        sequence = getArithmeticSequence(prime_perms)
        if sequence is not None:
            if not hasAnswer(answers, sequence):
                answers.append(sequence)
            if len(answers) > 2:
                break
    print(answers)
    print(''.join([str(i) for i in answers[1]]))


def run():
    findAnswer49()




