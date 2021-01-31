import numpy as np
import math


def solution():
    counter = 0
    for i in range(23, 101):
        for j in range(i):
            if np.math.factorial(i) / (np.math.factorial(j) * np.math.factorial(i - j)) > 1000000:
                counter += 1
    return counter


def run():
    # print(solution())
    # print(math.factorial(23))
    n = 23
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
    print(fact)
