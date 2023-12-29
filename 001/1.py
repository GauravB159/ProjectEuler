from pelib.basic import timed

@timed
def process(limit):
    return sum((x for x in range(limit) if x % 3 == 0 or x % 5 == 0))

process(1000)