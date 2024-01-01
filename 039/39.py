from pelib.basic import timed

@timed
def process(n):
    max_ = 0
    result = 0
    for p in range(3, n + 1):
        count = 0
        for i in range(1, p):
            for j in range(i + 1, p):
                c = p - i - j
                if c < i or c < j:
                    break
                if c * c == i * i + j * j:
                    count += 1
        if count > max_:
            max_ = count
            result = p
    return result
process(1000)