from utilz.prime_utils import is_prime


def spiral_diagonals_prime_ratios(n):
    diagonals = [1]
    multiplier = 2
    primes = []
    while True:
        for i in range(4):
            d = (diagonals[-1] + multiplier)
            diagonals.append(d)
            if is_prime(d):
                primes.append(d)
        if len(primes) / len(diagonals) < n:
            print(len(primes) / len(diagonals))
            return multiplier + 1
        multiplier += 2


def run():
    print(spiral_diagonals_prime_ratios(.10))
