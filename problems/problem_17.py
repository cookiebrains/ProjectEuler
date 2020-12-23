from utilz.numbers_dict import numbers_dict as dict


def first_nineteen():
    nums = []
    for i in range(1, 20):
        nums.append(dict[i])
    return nums


def twenty_through_ninety_nine():
    nums = []
    for k in range(2, 10):
        nums.append(dict[k * 10] * 10)
    for x in range(2, 10):
        for i in range(1, 10):
            nums.append(dict[i])
    return nums


def one_hundred_through_one_thousand():
    nums = []
    for k in range(1, 10):
        nums.append(dict[k * 100] * 100)
        nums.append('and' * 99)
        for i in range(1, 20):
            nums.append(dict[i])
        for m in range(2, 10):
            nums.append(dict[m * 10] * 10)
        for x in range(2, 10):
            for i in range(1, 10):
                nums.append(dict[i])

    return nums


def join_nums(nums):
    x = ''.join(nums)
    return x


def run():
    a = len(join_nums(first_nineteen()))
    print((join_nums(first_nineteen())))
    b = len(join_nums(twenty_through_ninety_nine()))
    print((join_nums(twenty_through_ninety_nine())))
    print(join_nums(one_hundred_through_one_thousand()))
    c = len(join_nums(one_hundred_through_one_thousand()))
    total = [a, b, c, 11]
    print(a)

    print(sum(total))
