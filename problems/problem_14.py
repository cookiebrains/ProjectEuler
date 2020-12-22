import progressbar


def collatz_sequence(num):
    counter = 0
    a = num
    while True:
        if a == 1:
            print(f'final counter value: {counter}')
            return counter
        elif a % 2 == 0:
            print(f'counter before yield: {counter}')
            yield a / 2
            counter += 1
            a = a / 2
        else:
            print(f'counter before yield: {counter}')
            yield (3 * a) + 1
            counter += 1
            a = (3 * a) + 1


def get_collatz_sequence(num):
    a = num
    while True:
        if a == 1:
            yield 1
        elif a % 2 == 0:
            yield a / 2
            a = a / 2
        else:
            yield (3 * a) + 1
            a = (3 * a) + 1


def get_collatz_count(num):
    count = 0
    for collatz_num in get_collatz_sequence(num):
        count += 1
        if collatz_num == 1:
            break
    return count


def run():
    highest_count = 0
    starting_num = 1
    for num in progressbar.progressbar(range(500000, 550000)):
        if get_collatz_count(num) > highest_count:
            highest_count = get_collatz_count(num)
            starting_num = num
    print(highest_count)
    print(starting_num)
