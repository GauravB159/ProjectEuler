from pelib.basic import timed

@timed
def process(n):
    for i in range(1, 1_000_000):
        check = set(str(i))
        for j in range(2, n + 1):
            check = check.intersection(set(str(j * i)))
        if len(check) == len(str(i)):
            return i


process(6)