def is_same_digits(num1, num2):
    original = list(str(num1))
    while str(num2 % 10) in original:
        original.remove(str(num2 % 10))
        num2 = int(num2 / 10)
    if len(original) == 0 and num2 == 0:
        return True
    else:
        return False


# def solution():
#     for num in range(1, 100000000000):
#         if is_same_digits(num, num * 2):
#             if is_same_digits(num, num * 3):
#                 if is_same_digits(num, num * 4):
#                     if is_same_digits(num, num * 5):
#                         if is_same_digits(num, num * 6):
#                             return [num, num*2, num*3, num*4, num*5, num*6]

def solution():
    n = 1
    j = 2
    while True:
        if is_same_digits(n, n * j):
            j += 1
            if j == 7:
                return n
        else:
            n += 1




def run():
    print(solution())
