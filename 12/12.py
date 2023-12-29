from pelib import timed, getPrimes, getNumberOfFactors

@timed
def process(n):
    i = 1
    primes = getPrimes(1_000_00)
    while True:
        triangle = (i * (i + 1)) / 2
        num_factors = getNumberOfFactors(triangle, primes)
        if num_factors > n:
            break
        i += 1
    return int(triangle)

print(process(500))