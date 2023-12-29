from pelib import timed

@timed
def process(n):
    number = open("./input.txt").read().split("\n")
    number = "".join(number)
    max_ = 1
    for i, digit in enumerate(number[:1-n]):
        prod = int(digit)
        for j in range(1, n):
            prod *= int(number[i + j])
        max_ = max(max_, prod)
    return max_

print(process(13))