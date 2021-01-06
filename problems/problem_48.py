def get_power_to_powers():
    i = 1
    while True:
        yield i**i
        i += 1


def get_sum_of_power_to_powers(highest_power):
    counter = 0
    sum_of_powers = 0
    for item in get_power_to_powers():
        if counter == highest_power:
            return sum_of_powers
        counter += 1
        sum_of_powers += item


def run():
    print(str(get_sum_of_power_to_powers(1000))[-10:])
