from lib import sumOfFirst, sumOfFirstSquared


def process(n):
    return int(sumOfFirst(n) * sumOfFirst(n) - sumOfFirstSquared(n))

print(process(100))