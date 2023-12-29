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

def getPrimeFactorization(number):
    factorization = {}
    factors = getPrimeFactors(number)
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