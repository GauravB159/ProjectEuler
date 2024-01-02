from pelib.basic import timed, getPrimes

@timed
def process(n):
    primes = getPrimes(n)
    primeMap = {x: True for x in primes}
    max_ = 0
    result = 0
    for i in range(len(primes)):
        sum_ = primes[i]
        for j in range(i + 1, len(primes)):
            sum_ += primes[j]
            if sum_ > n:
                break
            if sum_ in primeMap:
                consecutive = j - i
                if max_ < consecutive:
                    max_ = consecutive
                    result = sum_
    return result


process(1000000)