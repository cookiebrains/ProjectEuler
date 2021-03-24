import math

def is_triangle(x):
    if is_square(8 * x + 1) and (8 * x - 1) % 2 != 0:
        return True
    else:
        return False


def is_square(x):
    root = math.sqrt(x)
    if root - int(root) == 0:
        return True
    else:
        return False


def is_pentagonal(x):
    if is_square(24 * x + 1) and (1 + math.sqrt(24 * x + 1)) % 6 == 0:
        return True
    else:
        return False


def is_hexagonal(x):
    if is_square(8 * x + 1) and (1 + math.sqrt(8 * x + 1)) % 4 == 0:
        return True
    else:
        return False


def get_octagonals(lower_lim, upper_lim):
    octagonals = []
    for i in range(lower_lim, upper_lim):
        octagonals.append(i * (3 * i - 2))
    return octagonals


def get_heptagonals(lower_lim, upper_lim):
    heptagonals = []
    for i in range(lower_lim, upper_lim):
        heptagonals.append(int((i * (5 * i - 3)) / 2))
    return heptagonals


def get_all_candidates():
    candidates = []
    for num in range(1000, 10000):
        if is_triangle(num):
            candidates.append([3, num])
    for num in range(1000, 10000):
        if is_square(num):
            candidates.append([4, num])
    for num in range(1000, 10000):
        if is_pentagonal(num):
            candidates.append([5, num])
    for num in range(1000, 10000):
        if is_hexagonal(num):
            candidates.append([6, num])
    for num in get_heptagonals(21, 64):
        candidates.append([7, num])

    return candidates


def is_cyclical(num1, num2):
    num1 = list(str(num1))
    num2 = list(str(num2))
    if num1[-1] == num2[1] and num1[-2] == num2[0]:
        return True
    else:
        return False


def check_one_candidate(item, candidates):
    candidates = candidates
    twos = branches_of_branch(item, candidates)
    threes = []
    fours = []
    fives = []
    sixes = []
    for branch in twos:
        three = branches_of_branch(branch, candidates)
        for x in three:
            threes.append(x)
    for branch in threes:
        four = branches_of_branch(branch, candidates)
        for x in four:
            fours.append(x)
    for branch in fours:
        five = branches_of_branch(branch, candidates)
        for x in five:
            fives.append(x)
    for branch in fives:
        six = branches_of_branch(branch, candidates)
        for x in six:
            sixes.append(x)

    return sixes


# Candidates = master list
def branches_of_branch(branch_so_far, candidates):
    new_branches = []
    tags_used = []
    nums_used = []

    # Keep track of "used" candidates
    for item in branch_so_far:
        tags_used.append(item[0])
    # Keep track of "used" numbers
    for item in branch_so_far:
        nums_used.append(item[1])

    for tag_number_pair in candidates:
        if tag_number_pair[0] not in tags_used \
                and tag_number_pair[1] not in nums_used \
                and is_cyclical(branch_so_far[-1][1], tag_number_pair[1]):
            new_branch = branch_so_far.copy()
            new_branch.append(tag_number_pair)
            new_branches.append(new_branch)

    return new_branches


def solution():
    # get octagonals to loop through
    octagonals = []
    for num in get_octagonals(19, 59):
        octagonals.append([8, num])
    candidates = get_all_candidates()
    for oct_pair in octagonals:
        sixes = check_one_candidate([oct_pair], candidates)
        for six_branch in sixes:
            if is_cyclical(six_branch[5][1], six_branch[0][1]):
                return six_branch


def run():
    print(solution())
    sum = 0
    for item in solution():
        sum += item[1]
    print(sum)



