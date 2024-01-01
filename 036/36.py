from pelib.basic import timed

@timed
def process(n):
    result = 0
    for i in range(n):
        str_i = str(i)
        if str_i == str_i[::-1]:
            if bin(i)[2:] == bin(i)[2:][::-1]:
                result += i
    return result
process(1_000_000)