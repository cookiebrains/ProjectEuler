def generate_ao_list(nth_term):
    ao_list = [2, 1]
    two_multiple = 2
    while len(ao_list) < nth_term:
        ao_list.append(two_multiple)
        ao_list.append(1)
        ao_list.append(1)
        two_multiple += 2

    ao_list = ao_list[:nth_term]
    return ao_list


def find_nth_numerator(num):
    ao_list = generate_ao_list(num)
    n = ao_list.pop()

    m = ao_list.pop()
    numerator = 1
    while True:
        numerator, n = n, n * m + numerator
        if len(ao_list) == 1:

            return 2 * n + numerator
        else:
            m = ao_list.pop()


def run():
    solution = 0
    number_string = str(find_nth_numerator(100))
    for num in number_string:
        solution += int(num)
    print(solution)
