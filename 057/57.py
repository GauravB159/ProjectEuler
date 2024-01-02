from pelib.basic import timed

@timed
def process(n):
    base_num = 1
    base_denom = 1
    count = 0
    for i in range(n):
        temp_base_num = base_denom
        base_denom = base_denom + base_num
        base_num = temp_base_num + base_denom
        if len(str(base_num)) > len(str(base_denom)):
            count += 1
    return count

process(1000)