from pelib.basic import timed

@timed
def process(n):
    answer = "1"
    for i in range(2, n + 1):
        next_answer = ""
        carry = 0
        for j, _ in enumerate(answer):
            pos = len(answer) - j - 1
            next = int(answer[pos]) * i + carry
            next_answer = str(next % 10) + next_answer
            carry = next // 10
        if carry > 0:
            answer = str(carry) + next_answer
        else:
            answer = next_answer
    return sum([int(x) for x in answer])

process(100)