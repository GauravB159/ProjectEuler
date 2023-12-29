from pelib.basic import timed

@timed
def process():
    text = open("input.txt").read().split("\n")
    carry = 0
    answer = ""
    for i in range(len(text[0])):
        pos = len(text[0]) - i - 1
        sum_ = 0
        for str_ in text:
            sum_ += int(str_[pos])
        sum_ += carry
        answer = str(sum_ % 10) + answer
        carry = sum_ // 10
    if carry > 0:
        answer = str(carry) + answer
    return answer[:10]

process()