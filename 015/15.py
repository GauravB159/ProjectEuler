from pelib.basic import timed

@timed
def process(n):
    cache = {}
    def traverse(point):
        if point.real > n or point.imag > n:
            return 0
        if point.real == n and point.imag == n:
            return 1
        if cache.get(point, 0):
            return cache[point]
        sum_ = 0
        sum_ += traverse(point + 1j)
        sum_ += traverse(point + 1)
        cache[point] = sum_
        return sum_
    return traverse(0 + 0j)

process(20)