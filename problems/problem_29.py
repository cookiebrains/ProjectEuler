def solution():
    big_list = []
    for a in range(2, 101):
        for b in range(2, 101):
            if (a ** b) not in big_list:
                big_list.append(a ** b)
    return big_list


def run():
    print(len(solution()))
