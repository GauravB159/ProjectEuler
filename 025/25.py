from pelib.basic import timed
from pelib.bignum import BigNum

@timed
def process(n):
    fib1 = BigNum(1)
    fib2 = BigNum(1)
    count = 2
    while(len(fib2.num) < n):
        fib2, fib1 = fib1.add(fib2), fib2
        count += 1
    return count


process(1000)