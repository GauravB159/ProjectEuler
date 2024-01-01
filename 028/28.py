from pelib.basic import timed

@timed
def process(n):
    count = 1
    sum_ = 1
    value = 1
    while count < n:
        count += 2
        diff = count - 1
        for _ in range(4):
            value += diff
            sum_ += value
    return sum_

process(1001)