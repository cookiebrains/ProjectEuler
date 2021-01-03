def is_pan_digital(num):
    changing_num = num
    check_set = set()
    while changing_num != 0:
        if changing_num % 10 != 0:
            check_set.add(changing_num % 10)
            changing_num = changing_num - (changing_num % 10)
            changing_num = changing_num / 10
        else:
            changing_num = changing_num / 10
    if len(check_set) == 9 == len(str(num)):
        return True
    else:
        return False


def candidates_from_three_digits():
    candidates = []
    for num in range(100, 1000):
        a = num
        b = num * 2
        c = num * 3
        abc = str(a) + str(b) + str(c)
        if is_pan_digital(int(abc)):
            candidates.append(abc)
    return candidates


def candidates_from_four_digits():
    candidates = []
    for num in range(1000, 10000):
        a = num
        b = num * 2
        ab = str(a) + str(b)
        if is_pan_digital(int(ab)):
            candidates.append(ab)
    return candidates


def run():
    print(candidates_from_three_digits())
    print(candidates_from_four_digits())
