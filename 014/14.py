from pelib.basic import timed

@timed
def process(n):
    cache = {}
    def collatz(number):
        if number == 1:
            return 1
        if cache.get(number, False):
            return cache[number]
        chain = 1
        if number % 2 == 0:
            chain += collatz(number / 2)
        else:
            chain += collatz(3 * number + 1)
        cache[number] = chain
        return chain
    
    max_ = 0
    result = 0
    for i in range(1, n):
        chain = collatz(i)
        if chain > max_:
            max_ = chain
            result = i
    return result

process(1000000)