from pelib.basic import timed, getPrimes

@timed
def process(n):
    primes = getPrimes(n)
    checkPrimes = {}
    for p in getPrimes(100000):
        checkPrimes[p] = 1
    
    possiblities = set()
    for i in range(n):
        for j in primes:
            possiblities.add((i, j))
            possiblities.add((-i, j))
    
    count = 1
    values = {}
    while(len(possiblities) > 1):
        remove = set()
        for possibility in possiblities:
            check = count * count + count * possibility[0] + possibility[1]
            if not checkPrimes.get(check, False):
                values[possibility] = count
                remove.add(possibility)
        possiblities = possiblities.difference(remove)
        count += 1
    return list(possiblities)[0][0] * list(possiblities)[0][1]

process(1000)