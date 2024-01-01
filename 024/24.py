from pelib.basic import factorial, timed

@timed
def process(n, r):
    numbers = list(range(n + 1))
    answer = ""
    r = r - 1
    while(len(numbers) > 1):
        total_possibilities = factorial(len(numbers) - 1)
        pos = int((r / total_possibilities))
        print(pos, r, total_possibilities)
        r = r % total_possibilities
        answer = answer + str(numbers[pos])
        numbers.remove(numbers[pos])
    answer = answer + str(numbers[0])
    return answer
process(9, 1_000_000)
