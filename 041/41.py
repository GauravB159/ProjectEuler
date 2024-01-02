from pelib.basic import timed, factorial, isPrime

def getLexicographicNumber(n, r):
    numbers = list(range(1, n + 1))
    answer = ""
    r = r - 1
    while(len(numbers) > 1):
        total_possibilities = factorial(len(numbers) - 1)
        pos = int((r / total_possibilities))
        r = r % total_possibilities
        answer = answer + str(numbers[pos])
        numbers.remove(numbers[pos])
    answer = answer + str(numbers[0])
    return answer

@timed
def process():
    for i in range(7, 2, -1):
        possibilities = factorial(i)
        for possibility in range(possibilities - 1, 0, -1):
            num = int(getLexicographicNumber(i, possibility))
            if isPrime(num):
                return num
    
process()