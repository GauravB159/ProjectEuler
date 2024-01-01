from pelib.basic import timed

@timed
def process():
    text = open("input.txt").read().split(",")
    text.sort()
    result = sum([sum([(ord(y) - ord('A') + 1) for y in x[1:-1]]) * (i + 1) for i, x in enumerate(text)])
    return result

process()