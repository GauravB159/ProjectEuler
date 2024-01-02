from pelib.basic import timed

@timed
def process():
    count = 0
    for i in range(1, 10_000):
        num = i
        lychrel = True
        for j in range(49):
            rev = int(str(num)[::-1])
            if rev == num and num != i:
                lychrel = False
                break
            else:
                num = num + rev
        print()
        if lychrel:
            count += 1
    return count

process()