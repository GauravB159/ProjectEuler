from pelib.basic import timed

@timed
def process(n):
    digit_configurations = {}
    for i in range(1, 10000):
        value = ''.join(sorted(str(i ** 3)))
        if value not in digit_configurations:
            digit_configurations[value] = []
        digit_configurations[value].append(i)
        if len(digit_configurations[value]) == n:
            return digit_configurations[value][0] ** 3

process(5)