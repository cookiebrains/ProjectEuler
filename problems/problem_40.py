def generate_counting_string(upper_lim):
    number_string = '1'
    for i in range(2, upper_lim):
        number_string = number_string + f'{i}'
    return number_string


def solution(number_string):
    sol = 1
    for i in range(7):
        sol *= int(number_string[(10 ** i) - 1])

    return sol


def run():
    a = generate_counting_string(200000)
    print(solution(a))
