from pelib import getPrimes, timed

@timed
def process(n):
    return sum(getPrimes(n))

print(process(2_000_000))