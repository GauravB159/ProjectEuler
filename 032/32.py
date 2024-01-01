from pelib.basic import timed

@timed
def process():
    result = {}
    for i in range(1, 10000):
        str_i = str(i)
        if len(set(str_i)) != len(str_i) or '0' in str_i:
            continue
        for j in range(1, 1000):
            str_j = str(j)
            if len(set(str_i + str_j)) != len(str_i + str_j) or '0' in str_j:
                continue
            mult = str(i * j)
            if len(set(str_i + str_j + mult)) != len(str_i + str_j + mult) or '0' in mult:
                continue
            if len(str_i + str_j + mult) == 9:
                result[mult] = 1
    print(result)
    return sum([int(x) for x in result.keys()])

process()