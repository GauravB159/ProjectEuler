from pelib.basic import timed

@timed
def process(n):
    triangle = set([int((n * (n + 1)) / 2) for n in range(1, n)])
    pentagonal = set([int((n * (3 * n - 1)) / 2) for n in range(1, n)])
    hexagonal = set([int(n * (2 * n - 1)) for n in range(1, n)])
    print(triangle.intersection(pentagonal).intersection(hexagonal))

process(100000)