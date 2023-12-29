def getPrimes(limit):
    primes = [False] * (limit + 1)
    i = 2
    while i*i < limit:
        for j in range(2, limit // i + 1):
            primes[j * i] = True
        i += 1
    return [i for i, x in enumerate(primes) if not x][2:]