from pelib.basic import timed, getLexicographicNumber, factorial

@timed
def process():
    result = 0
    for i in range(factorial(10)):
        number = getLexicographicNumber(9, i, 0)
        if int(number[1:4]) % 2 != 0:
            continue
        if int(number[2:5]) % 3 != 0:
            continue
        if int(number[3:6]) % 5 != 0:
            continue
        if int(number[4:7]) % 7 != 0:
            continue
        if int(number[5:8]) % 11 != 0:
            continue
        if int(number[6:9]) % 13 != 0:
            continue
        if int(number[7:10]) % 17 != 0:
            continue
        result += int(number)
    return result

process()