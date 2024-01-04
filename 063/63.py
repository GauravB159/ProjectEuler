from pelib.basic import timed

@timed
def process():
    count = 0
    for i in range(1, 10):
        for j in range(1, 25):
            if len(str(i ** j)) == j:
                count += 1
    return count

process()