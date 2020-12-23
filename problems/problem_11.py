from functools import reduce
from operator import mul


def get_number_array_from_file():
    two_dimensional_number_array = []
    with open("input_files/grid.txt") as file:
        # x = [l.rstrip("\n") for l in file]
        # return x
        for line in file:
            two_dimensional_number_array.append(string_to_number_list(line))
    return two_dimensional_number_array


# Sample of alternate to pass to map call
def string_to_int(s):
    return int(s)


def string_to_number_list(s):
    string_list = s.split()
    # numbers = list(map(string_to_int, string_list))
    # numbers = list(map(lambda x: int(x), string_list))
    numbers = list(map(int, string_list))
    # print(numbers)
    return numbers


def product(iterable):
    """Return the product of the numbers in the iterable."""
    return reduce(mul, iterable, 1)


def horizontal_max(grid):
    a = max(product(grid[i][j + k] for k in range(4))
            for i in range(0, 20)
            for j in range(17))
    return a


def vertical_max(grid):
    a = max(product(grid[i + k][j] for k in range(4))
            for i in range(0, 17)
            for j in range(20))
    return a


def leading_diagonal(grid):
    a = max(product(grid[i + k][j + k] for k in range(4))
            for i in range(0, 17)
            for j in range(17))
    return a


def trailing_diagonal(grid):
    a = max(product(grid[i - k][j + k] for k in range(4))
            for i in range(3, 20)
            for j in range(17))
    return a


def run():
    # a = get_the_lines_from_file()
    # b = separate_items_in_list_of_lines(a)
    # print(b)
    # string_to_number_list(practice)
    number_array = get_number_array_from_file()
    # print(number_array)
    # print(horizontal_max(number_array))
    # print(vertical_max(number_array))
    # print(leading_diagonal(number_array))
    # print(trailing_diagonal(number_array))
    answer = max(horizontal_max(number_array),
                 vertical_max(number_array),
                 leading_diagonal(number_array),
                 trailing_diagonal(number_array))
    print(f'the answer is {answer}')

