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
    factors = getFactors(number)
    return [x for x in factors if primes.get(x, False)]

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

def getFactors(n):
    count = 1
    factors = set()
    while count * count <= n:
        if n % count == 0:
            factors.add(count)
            factors.add(n // count)
        count += 1
    return list(factors)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def isPrime(n):
    count = 2
    while count * count <= n:
        if n % count == 0:
            return False
        count += 1
    return True


def getLexicographicNumber(n, r, start = 1):
    numbers = list(range(start, n + 1))
    answer = ""
    r = r - 1
    while(len(numbers) > 1):
        total_possibilities = factorial(len(numbers) - 1)
        pos = int((r / total_possibilities))
        r = r % total_possibilities
        answer = answer + str(numbers[pos])
        numbers.remove(numbers[pos])
    answer = answer + str(numbers[0])
    return answer

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))