from pelib import timed

@timed
def process(limit):
    return sum((x for x in range(limit) if x % 3 == 0 or x % 5 == 0))

print(process(1000))