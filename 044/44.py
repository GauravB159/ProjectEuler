from pelib.basic import timed

@timed
def process():
    pentagonal = {int(n * (3 * n - 1) / 2): True for n in range(1, 10000)}
    for i in pentagonal:
        for j in pentagonal:
            if not pentagonal.get(i + j, False):
                continue
            if not pentagonal.get(i - j, False):
                continue
            print(abs(i - j))

process()