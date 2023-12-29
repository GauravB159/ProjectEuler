from lib import getPrimeFactorization
from math import pow

def process(limit):
    factors = []
    for i in range(limit):
        factors.append(getPrimeFactorization(i + 1))

    max_factors = {}
    for factor in factors:
        for key in factor:
            if not max_factors.get(key):
                max_factors[key] = 0
            if factor[key] > max_factors[key]:
                max_factors[key] = factor[key]
    result = 1
    for key in max_factors:
        result *= pow(key, max_factors[key])
    return int(result)

print(process(20))