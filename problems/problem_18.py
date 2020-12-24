def get_number_array_from_file(file_path):
    two_dimensional_number_array = []
    with open(file_path) as file:
        for line in file:
            two_dimensional_number_array.append(string_to_number_list(line))
    return two_dimensional_number_array


def string_to_number_list(s):
    string_list = s.split()
    numbers = list(map(int, string_list))
    return numbers


practice_triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


def learn_two_dimensional_indexing(triangle):
    sample = []
    i = len(triangle) - 1
    for number in triangle[i]:
        sample.append(triangle[i].index(number))
    return sample


def new_bottom_row(triangle):
    new_row = []
    i = len(triangle) - 2
    for number in triangle[i]:
        j = triangle[i].index(number)
        new_row.append(max((number + triangle[i + 1][j]), (number + triangle[i + 1][j + 1])))
    return new_row


def get_new_row_and_drop_bottom_two(triangle):
    shrinking_triangle = triangle
    new_row = new_bottom_row(triangle)
    shrinking_triangle = shrinking_triangle[:(len(shrinking_triangle) - 2)]
    shrinking_triangle.append(new_row)
    return shrinking_triangle


def solution(triangle):
    while len(triangle) > 1:
        triangle = get_new_row_and_drop_bottom_two(triangle)
    return triangle


def run():
    a = (get_number_array_from_file("input_files/triangle_of_numbers.txt"))
    print(a)
    # print(a)
    # print(new_bottom_row(practice_triangle))
    # print(learn_two_dimensional_indexing(practice_triangle))
    print(solution(a))
