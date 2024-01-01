from pelib.basic import timed

@timed
def process(n):
    possibilities = [1, 2, 5, 10, 20, 50, 100, 200]
    visited = {}
    def recurse(remain, denominations):
        if remain < 0:
            return 0
        if tuple(denominations) in visited:
            return 0
        visited[tuple(denominations)] = True
        if remain == 0:
            return 1
        answer = 0
        for i, possibility in enumerate(possibilities):
            new_denominations = denominations[:]
            new_denominations[i] += 1
            answer += recurse(remain - possibility, new_denominations)
        return answer
    return recurse(n, [0] * len(possibilities))

process(200)