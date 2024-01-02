from pelib.basic import timed, getPrimes

@timed
def process():
    primes = {x: True for x in getPrimes(10000)}
    for prime in primes:
        dts = str(prime)
        check_one = prime + 3330
        if len(dts) < 4:
            continue
        if check_one not in primes:
            continue
        check_two = prime + 6660
        if check_two not in primes:
            continue
        if set(dts) != set(str(check_one)):
            continue
        if set(dts) != set(str(check_two)):
            continue
        if prime == 1487:
            continue
        return dts + str(check_one) + str(check_two)

process()