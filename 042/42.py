from pelib.basic import timed

@timed
def process():
    text = open("input.txt").read().split(",")
    triangles = {int((n * (n + 1)) / 2): 1 for n in range(1, 20)}
    text = [triangles.get(sum([ord(y) - ord('A') + 1 for y in x[1:-1]]), 0) for x in text]
    return sum(text)

process()