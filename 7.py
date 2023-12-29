from lib import getPrimes

def process(n):
    primes = getPrimes(n * 20)
    return primes[n - 1]

print(process(10_001))