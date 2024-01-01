from pelib.basic import timed
from math import pow

@timed
def process(n):
    result = 0
    def recurse(number, sum_, level):
        nonlocal result
        if level > n + 1:
            return
        if len(number) > 1 and sum_ == int(number):
            result += int(number)
            print(number)
        for i in range(10):
            if level == 0 and i == 0:
                continue
            recurse(number + str(i), sum_ + pow(i, n), level + 1)
    recurse("", 0, 0)
    return result

process(5)