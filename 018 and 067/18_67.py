from pelib.basic import convert2DArrayToGrid, timed

@timed
def process(file):
    text = open(file).read().split("\n")
    text = [x.split(" ") for x in text]
    grid = convert2DArrayToGrid(text)
    cache = {}
    def traverse(point):
        if not grid.get(point, False):
            return 0
        if point in cache:
            return cache[point]
        sum_ = int(grid[point]) + max(traverse(point + 1), traverse(point + (1 + 1j)))
        cache[point] = sum_
        return sum_
    return traverse(0j)

print("Problem 18")
process("18.txt")

print("\n\nProblem 67")
process("67.txt")