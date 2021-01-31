def reversal(a):
    return a[::-1]


def is_palindrome(num):
    if str(num) == reversal(str(num)):
        return True


def is_lychrel(num):
    counter = 0
    check_num = num
    while counter < 51:
        test_num = check_num + int(reversal(str(check_num)))
        if is_palindrome(test_num):
            return False
        else:
            check_num = test_num
            counter += 1
            continue
    return True


def run():
    answer = 0
    for i in range(1, 10000):
        if is_lychrel(i):
            answer += 1
    print(answer)


2
