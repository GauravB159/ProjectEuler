from pelib.basic import timed
from math import gcd

@timed
def process():
    num = 1
    denom = 1
    for i in range(10, 100):
        str_i = str(i)
        for j in range(i + 1, 100):
            if i == j or i % 10 == 0:
                continue
            str_j = str(j)
            try:
                if str_i[0] == str_j[0]:
                    check = int(str_i[1]) / int(str_j[1])
                    if check == (i / j):
                        num *= i
                        denom *= j
                if str_i[0] == str_j[1]:
                    check = int(str_i[1]) / int(str_j[0])
                    if check == (i / j):
                        num *= i
                        denom *= j
                if str_i[1] == str_j[0]:
                    check = int(str_i[0]) / int(str_j[1])
                    if check == (i / j):
                        num *= i
                        denom *= j
                if str_i[1] == str_j[1]:
                    check = int(str_i[0]) / int(str_j[0])
                    if check == (i / j):
                        num *= i
                        denom *= j
            except ZeroDivisionError:
                continue
    return int(denom / gcd(num, denom))

process()