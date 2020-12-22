import math


def get_pythagorean_triplets(limits):
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if c is greater than
            # limit then break it
            if c > limits:
                break

            yield a, b, c

        m = m + 1




def do_work():
    for x, y, z in get_pythagorean_triplets(800):
        if x + y + z == 1000:
            print(x, y, z)


do_work()
