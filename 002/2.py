from pelib import timed

cache = {}
def fib(n):
    if cache.get(n):
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

@timed
def process(n):
    result = 0
    for i in range(n):
        check = fib(i)
        if check > 4_000_000:
            break
        if check % 2 == 0:
            result += check
    return result


process(100)