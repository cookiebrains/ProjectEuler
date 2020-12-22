def sum_of_consecutive_squares(n):
    summation = 0
    for i in range(1, n+1):
        summation += i**2
    return summation


def square_of_consecutive_nums(n):
    summation = 0
    for i in range(1, n+1):
        summation += i
    return summation ** 2


def get_solution(n):
    sum_of_squares = sum_of_consecutive_squares(n)
    square_of_sum = square_of_consecutive_nums(n)
    print(f'The solution is: {abs(sum_of_squares - square_of_sum)}')


def run():
    get_solution(100)
