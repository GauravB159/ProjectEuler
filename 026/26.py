from pelib.basic import timed

@timed
def process(n):
    max_ = 0
    max_number = 0
    for i in range(1, n):
        count = 0
        num = 1
        visited = {}
        answer = -1
        while(True):
            count += 1
            num = num * 10
            if num in visited:
                answer = count - visited[num]
                break
            visited[num] = count
            num = num % i
        if answer > max_:
            max_ = answer
            max_number = i
    return max_number

process(1000)