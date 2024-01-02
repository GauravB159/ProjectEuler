from pelib.basic import getPrimeFactors, timed, getPrimes

@timed
def process(n):
    primes = getPrimes(1000000)
    primesMap = {x: True for x in primes}
    pfs = [len(getPrimeFactors(x, primesMap)) for x in range(2, 1000000)]
    for i in range(len(pfs) - n):
        valid = True
        for j in range(n):
            if pfs[i + j] != n:
                valid = False
                break
        if valid:
            return i + 2

process(4)