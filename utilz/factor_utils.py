import math


# Includes 1 and the number passed
def get_factors(num):
    factors = [1, num]
    sqr_root_approximate = math.ceil(math.sqrt(num)) + 1
    for i in range(2, sqr_root_approximate + 1):
        if num % i == 0:
            if i not in factors:
                factors.append(i)
            second_factor = int(num / i)
            if second_factor not in factors:
                factors.append(second_factor)
    return sorted(factors)
