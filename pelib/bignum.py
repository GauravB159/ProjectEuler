class BigNum:
    def __init__(self, num: int):
        self.num = []
        while num > 0:
            self.num.append(num % 10)
            num = num // 10
        self.num = self.num[::-1]

    def add(self, additive):
        limit = max(len(self.num), len(additive.num))
        answer = []
        carry = 0
        left = self.num[::-1]
        right = additive.num[::-1]
        for i in range(limit):
            if i >= len(left):
                next_num = right[i] + carry
            elif i >= len(right):
                next_num = left[i] + carry
            else:
                next_num = left[i] + right[i] + carry
            carry = next_num // 10
            next_num = next_num % 10
            answer.append(next_num)
        while carry != 0:
            answer.append(carry % 10)
            carry = carry // 10
        self.num = answer[::-1]
        return self