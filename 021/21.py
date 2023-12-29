from pelib.basic import timed, getFactors

@timed
def process(n):
    result = set()
    for i in range(2, n):
        factors = getFactors(i)
        sum_ = sum(factors) - i
        reverseFactors = getFactors(sum_)
        reverse_sum = sum(reverseFactors) - sum_
        if reverse_sum == i and i != sum_:
            result.add(i)
    return sum(result)

process(10000)