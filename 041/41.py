from pelib.basic import timed, factorial, isPrime, getLexicographicNumber

@timed
def process():
    for i in range(7, 2, -1):
        possibilities = factorial(i)
        for possibility in range(possibilities - 1, 0, -1):
            num = int(getLexicographicNumber(i, possibility))
            if isPrime(num):
                return num
    
process()