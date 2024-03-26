from pelib.basic import timed

def get_period(number):
    a = int(number ** 0.5)
    numerator = 1
    denominator = a
    visited = {}
    visited[(numerator, denominator)] = True
    period = []
    while True:
        a = int(numerator / (number ** 0.5 - denominator))
        numerator = (number - (denominator ** 2)) // numerator
        denominator = numerator * a - denominator
        period.append(a)
        if (numerator, denominator) in visited:
            break
        visited[(numerator, denominator)] = True
    return period
    
@timed
def process(n):
    count = 0   
    for i in range(2, n + 1):
        if i ** 0.5 - int(i ** 0.5):
            length = len(get_period(i))
            if length % 2 == 1:
                count += 1
    return count

process(10000)