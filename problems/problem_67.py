def get_number_array_from_file(file_path):
    two_dimensional_number_array = []
    with open(file_path) as file:
        for line in file:
            two_dimensional_number_array.append(string_to_number_list(line))
    return two_dimensional_number_array


practice_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


def string_to_number_list(s):
    string_list = s.split()
    numbers = list(map(int, string_list))
    return numbers


def new_bottom_row(triangle):
    upper = triangle[len(triangle) - 2]
    lower = triangle[len(triangle) - 1]
    new_row = new_row_from_two(upper, lower)
    return new_row


def new_row_from_two(upper_row, lower_row):
    new_row = []
    for i in range(0, len(upper_row)):
        lower_left = lower_row[i]
        lower_right = lower_row[i + 1]
        new_row.append(max(upper_row[i] + lower_left, upper_row[i] + lower_right))
    return new_row


a = [23, 45, 67, 90, 25, 80]
b = [98, 65, 76, 7, 45, 201, 35]


def get_new_row_and_drop_bottom_two(triangle):
    shrinking_triangle = triangle
    new_row = new_bottom_row(triangle)
    # shrinking_triangle = shrinking_triangle[:(len(shrinking_triangle) - 2)]
    shrinking_triangle = shrinking_triangle[:-2]
    shrinking_triangle.append(new_row)
    print(new_row)
    return shrinking_triangle


def solution(triangle):
    while len(triangle) > 1:
        triangle = get_new_row_and_drop_bottom_two(triangle)
    return triangle


def run():
    big_triangle = (get_number_array_from_file("input_files/p067_triangle.txt"))
    solution(big_triangle)

    # l = [1, 2, 3]
    # l = l[:-1]
    # print(l)

    # practice_row = new_row_from_two(big_triangle[98], big_triangle[99])
    # print(practice_row)
    # print(len(practice_row))
    # numbers = [1, 2, 3, 3, 4, 5, 6]
    # for num in numbers:
    #     print(f'For number {num}, numbers.index is {numbers.index(num)}')
