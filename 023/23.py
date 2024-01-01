from pelib.basic import getFactors, timed

@timed
def process():
    limit = 28123
    abundants = []
    for i in range(2, limit):
        total = sum(getFactors(i)) - i
        if i < total:
            abundants.append(i)
    
    non_abundants_sum = [True] * limit
    for i in abundants:
        for j in abundants:
            if i + j < limit:
                non_abundants_sum[i + j] = False
    
    result = [i for i, x in enumerate(non_abundants_sum) if x]
    return sum(result)

process()