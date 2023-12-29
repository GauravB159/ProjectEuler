import time
import math

def getPrimes(limit):
    primes = [False] * (limit + 1)
    i = 2
    while i*i < limit:
        for j in range(2, limit // i + 1):
            primes[j * i] = True
        i += 1
    return [i for i, x in enumerate(primes) if not x][2:]

def checkPalindrome(number):
    return str(number) == str(number)[::-1]

def getPrimeFactors(number, primes = []):
    if not primes:
        primes = getPrimes(number + 1)
    return [x for x in primes if number % x == 0]

def getPrimeFactorization(number, primes = False):
    factorization = {}
    factors = getPrimeFactors(int(number), primes)
    for factor in factors:
        count = 0
        while number % factor == 0:
            count += 1
            number = number / factor
        factorization[factor] = count
    return factorization

def sumOfFirst(n):
    return (n * (n + 1)) / 2

def sumOfFirstSquared(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

def timed(f):
    def inner(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print(f"Processing time: {(time.time() - start) * 1000:.2f}ms")
        print()
        print(f"Result: {result}")
    return inner

def convert2DArrayToGrid(arr):
    grid = {}
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            grid[complex(i, j)] = col
    return grid

def getNumberOfFactors(n, primes = False):
    pf = getPrimeFactorization(n, primes)
    num_factors = math.prod([(x + 1) for x in pf.values()])
    return num_factors