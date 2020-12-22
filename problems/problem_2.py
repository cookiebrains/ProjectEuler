def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def generateFibList(upper_lim):
    fib_list = []
    for x in fibonacci():
        if x < upper_lim:
            fib_list.append(x)
        elif x > upper_lim:
            break
    return fib_list


def evensInList(candidates):
    even_list = []
    for i in candidates:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def run():
    even_fibs_added = 0
    for i in evensInList(generateFibList(4000000)):
        even_fibs_added += i
    print(even_fibs_added)
