from lib import check_palindrome

max_ = 0

for i in range(100, 1000):
    for j in range(i + 1, 1000):
        if check_palindrome(i * j) and i * j > max_:
            max_ = i * j

print(max_)