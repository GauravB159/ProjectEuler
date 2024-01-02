from pelib.basic import getPrimes, timed, isPrime

@timed
def process():
    count = 1
    value = 1
    total_count = 1
    prime_count = 0
    while count < 100000:
        count += 2
        diff = count - 1
        total_count += 4
        for _ in range(4):
            value += diff
            if isPrime(value):
                prime_count += 1
        if prime_count < 0.1 * total_count:
            return count
    return -1

process()