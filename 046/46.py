from pelib.basic import timed, getPrimes
from math import sqrt

@timed
def process():
    primes = {x: True for x in getPrimes(100000)}
    for i in range(3, 1000000, 2):
        if primes.get(i):
            continue
        present = False
        for j in range(1, 10000):
            check = i - 2 * j * j
            if primes.get(check):
                present = True
                break
        if not present:
            return i
process()