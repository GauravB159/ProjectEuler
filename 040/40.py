from pelib.basic import timed
import math

def getByIndex(idx, totals):
    for i, total in enumerate(totals):
        if idx < total:
            offset = idx // (i+1)
            inner_offset = idx % (i+1)
            number = pow(10, i) + offset
            digit = str(number)[inner_offset]
            return int(digit)
        else:
            idx -= total

@timed
def process():
    idxs = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]
    totals = [0]
    for i in range(1, 7):
        totals.append(i * (pow(10, i) - pow(10, i - 1)))
    return math.prod([getByIndex(x - 1, totals[1:]) for x in idxs])

process()