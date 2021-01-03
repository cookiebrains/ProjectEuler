def reversal(a):
    return a[::-1]


def binary_of_integer(n):
    binary = bin(n)
    binary = binary[2:]
    return binary


def solution():
    solution_sum = 0
    for num in range(1000000):
        if str(num) == reversal(str(num)) and binary_of_integer(num) == reversal(binary_of_integer(num)):
            solution_sum += num
    return solution_sum


def run():
    print(solution())
