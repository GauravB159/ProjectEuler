from pelib.basic import timed
import math

@timed
def process(l, u):
    distinct = set()
    for i in range(l, u + 1):
        for j in range(l, u + 1):
            distinct.add(math.pow(i, j))
    return len(distinct)

process(2, 100)