from pelib.basic import timed

@timed
def process(n):
    result = 0
    for i in range(1, n + 1):
        result += pow(i, i)
    return str(result)[-10:]

process(1000)