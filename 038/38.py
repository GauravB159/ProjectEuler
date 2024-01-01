from pelib.basic import timed

@timed
def process():
    max_ = 0
    for i in range(1, 100000):
        check = ""
        for j in range(1, 20):
            check += str(i * j)
            if '0' in check:
                break
            if len(set(check)) < len(check):
                break
            if len(check) == 9 and j > 1:
                if int(check) > max_:
                    print(i, j)
                    max_ = int(check)
    return max_
process()