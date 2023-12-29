from pelib.basic import convert2DArrayToGrid, timed

@timed
def process(n):
    text = open("input.txt").read().split("\n")
    text = [[int(y) for y in x.split(" ")] for x in text]
    grid = convert2DArrayToGrid(text)
    directions = [1j, 1, 1 + 1j, 1 - 1j]
    max_ = 0
    for point in grid:
        for direction in directions:
            prod = grid[point]
            next_point = point
            for _ in range(1, n):
                next_point = next_point + direction
                prod *= grid.get(next_point, 0)
            max_ = max(max_, prod)
    return max_


process(4)
