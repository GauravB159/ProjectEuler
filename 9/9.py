from pelib import timed

@timed
def process(n):
    for i in range(1, n):
        for j in range(i + 1, n):
            check = n * (n - 2 * i - 2 * j) + 2 * i * j
            if not check:
                return i * j * (n - i - j)
            
print(process(1000))