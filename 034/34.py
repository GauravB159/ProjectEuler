from pelib.basic import timed, factorial

@timed
def process():
    factorials = [factorial(x) for x in range(10)]
    result = 0
    def recurse(number, sum_, level):
        nonlocal result
        if level > 5:
            return
        if len(number) > 1 and int(number) == sum_:
            result += sum_
            print(number, sum_)
        for i in range(10):
            if level == 0 and i == 0:
                continue
            recurse(number + str(i), sum_ + factorials[i], level + 1)
        return
    recurse("", 0, 0)
    return result

process()