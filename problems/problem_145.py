def reversal(a):
    return a[::-1]


def add_reverse(num):
    product = num + int((reversal(str(num))))
    return product


def are_digits_odd(num):
    number_string = str(num)
    for i in number_string:
        int_num = int(i)
        if int_num % 2 == 0:
            return False
    return True


def run():
    # solutions = []
    counter = 0
    for num in range(1, 1000000000):
        if num % 10 == 0:
            continue
        reverse_sum = add_reverse(num)
        if are_digits_odd(reverse_sum):
            counter += 1
    print(counter)
    #         solutions.append(num)
    # print(solutions)

    # counter for 1 billion was 608720, took around 5 minutes to process
