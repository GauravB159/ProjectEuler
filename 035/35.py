from pelib.basic import timed, getPrimes

@timed
def process(n):
    primes = {str(x): 1 for x in getPrimes(n)}
    count = 0
    for prime in primes:
        circular = True
        for _ in range(len(prime)):
            prime = prime[1:] + prime[0]
            if not primes.get(prime):
                circular = False
                break
        if circular:
            count += 1
    return count

process(1_000_000)