from pelib.basic import timed, nCr

@timed
def process(n, limit):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            check = nCr(i, j)
            if check > limit:
                count += 1
    return count

process(100, 1_000_000)