def factorial(n):
    result = 1
    for i in range(1, (n+1)):
        result = result * i
    return result


def add_digits(n):
    sum_of_digits = 0
    for item in str(n):
        sum_of_digits += int(item)
    return sum_of_digits


def run():
    print(add_digits(factorial(100)))
