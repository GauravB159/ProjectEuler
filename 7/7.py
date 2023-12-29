from pelib import getPrimes, timed

@timed
def process(n):
    primes = getPrimes(n * 20)
    return primes[n - 1]

print(process(10_001))