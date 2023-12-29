from lib import getPrimes
from math import sqrt

def getLargestPrimeFactor(number):
    primes = getPrimes(int(sqrt(number)))
    result = 0
    for prime in primes:
        if number % prime == 0:
            result = prime
    
    return result

print(getLargestPrimeFactor(600_851_475_143))