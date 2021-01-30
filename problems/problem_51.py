from utilz.prime_utils import *

primes = [2]
searched = set()


def create_placeholder(s, index):
    return s[0:index] + '*' + s[index + 1:]


def binary_search(prime):
    start = 0
    end = len(primes)
    middle = int((end + start) / 2)

    while start < end and primes[middle] != prime and middle < len(primes):
        if primes[middle] < prime:
            start = middle + 1
        else:
            end = middle - 1
        middle = int((end + start) / 2)

    if middle < len(primes) and primes[middle] == prime:
        return middle
    else:
        return -1


def run():
    wildcards = []

    def generate_wildcard_strings(s, index):
        if index > 0 and s not in searched:
            wildcards.append(s)
            searched.add(s)
        for x in range(index, len(s)):
            generate_wildcard_strings(create_placeholder(s, x), x + 1)

    for x in range(3, 1000000):
        found = False
        for i in range(0, len(primes)):
            if x % primes[i] == 0:
                found = True
                break
            if primes[i] * primes[i] > x:
                break
        if not found:
            primes.append(x)

    for x in range(0, len(primes)):
        wildcards = []
        # generate all possible wildcard strings for that prime
        generate_wildcard_strings(str(primes[x]), 0)
        # loop through all possible wildcard strings
        for y in range(1, len(wildcards)):
            count = 0
            # fill up the asterisk with 0-9
            for z in range(0, 10):
                num = int(wildcards[y].replace('*', str(z)))
                if len(str(num)) < len(wildcards[y]):
                    continue
                if binary_search(num) >= 0:
                    count += 1
            # if counter is at least 8 then print and exit program
            if count >= 8:
                print(primes[x])
                print(wildcards[y])
         