from pelib.basic import timed

def getDigitSum(n, power):
    answer = "1"
    for _ in range(power):
        next_answer = ""
        carry = 0
        for j, _ in enumerate(answer):
            pos = len(answer) - j - 1
            next = int(answer[pos]) * n + carry
            next_answer = str(next % 10) + next_answer
            carry = next // 10
        if carry > 0:
            answer = str(carry) + next_answer
        else:
            answer = next_answer
    return sum([int(x) for x in answer])

@timed
def process():
    max_ = 0
    for i in range(100):
        for j in range(100):
            sum_ = getDigitSum(i, j)
            if sum_ > max_:
                max_ = sum_
    return max_
    

process()