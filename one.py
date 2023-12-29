limit = 1000
answer = sum((x for x in range(limit) if x % 3 == 0 or x % 5 == 0))
print(answer)