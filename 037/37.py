from pelib.basic import timed, getPrimes

@timed
def process():
    primes = {str(x): 1 for x in getPrimes(1000000)}
    sum_ = 0
    for prime in primes:
        trunctable = True
        if len(prime) < 2:
            continue
        for i in range(1, len(prime)):
            left = prime[i:]
            right = prime[:-i]
            if not primes.get(left, False) or not primes.get(right, False):
                trunctable = False
                break
        if trunctable:
            sum_ += int(prime)
    return sum_
process()