from pelib import sumOfFirst, sumOfFirstSquared, timed

@timed
def process(n):
    return int(sumOfFirst(n) * sumOfFirst(n) - sumOfFirstSquared(n))

print(process(100))