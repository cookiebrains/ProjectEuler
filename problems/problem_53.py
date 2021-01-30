import numpy as np


def solution():
    counter = 0
    for i in range(23, 101):
        for j in range(i):
            if np.math.factorial(i) / (np.math.factorial(j) * np.math.factorial(i - j)) > 1000000:
                counter += 1
    return counter


def run():
    print(solution())

