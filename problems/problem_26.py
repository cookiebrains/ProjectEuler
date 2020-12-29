LIMIT = 5000


def run():
    max_len = 0  # The maximum length
    max_d = 1  # The 'd' that has maximum length

    for d in range(1, 1000):
        quotient = {0: 0}  # Stores the decimal quotient
        cur_value = 1  # Variable used to perform division as if by hand
        len_recur = 0  # Recurring length

        # Performing division as if by hand
        while cur_value not in quotient:  # while the value is not recurring
            len_recur += 1
            quotient[cur_value] = len_recur
            cur_value = (cur_value % d) * 10

        if not cur_value:
            continue

        # Remove number of values that do not recur
        len_recur -= quotient[cur_value]
        # quotient.clear()

        if len_recur > max_len:
            max_len = len_recur
            max_d = d

    print(max_d)

# def length_of_recurring_cycle(n):
#     digits_list = []
#     remainder = 1
#     divisor = 10 * remainder
#     while remainder != 0:
#         new_digit = int(divisor / n)
#         if new_digit not in digits_list or new_digit == 0:
#             digits_list.append(new_digit)
#             remainder = divisor - (n * new_digit)
#             divisor = 10 * remainder
#
#         else:
#             digits_list.append(new_digit)
#             break
#
#     return digits_list
#
#

