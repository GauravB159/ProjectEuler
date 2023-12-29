from pelib import checkPalindrome, timed

@timed
def process(l, u):
    max_ = 0

    for i in range(l, u):
        for j in range(i + 1, u):
            if checkPalindrome(i * j) and i * j > max_:
                max_ = i * j
    return max_

process(100, 1000)