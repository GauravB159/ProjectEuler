from pelib import getPrimes, timed
from math import sqrt

@timed
def process(number):
    primes = getPrimes(int(sqrt(number)))
    result = 0
    for prime in primes:
        if number % prime == 0:
            result = prime
    
    return result

process(600_851_475_143)