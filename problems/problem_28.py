def spiral_diagonals():
    diagonals = [1]
    multiplier = 2
    while multiplier < 1001:
        for i in range(4):
            diagonals.append((diagonals[-1] + multiplier))
        multiplier += 2
    return sum(diagonals)


def run():
    print(spiral_diagonals())
