from pelib.basic import timed

@timed
def process():
    months = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    start = 6 - 31
    count = 0
    for year in range(1901, 2001):
        for month in months:
            if month == 28 and year % 4 == 0:
                start += 29
                if year % 100 == 0:
                    start -= 1
                if year % 400 == 0:
                    start += 1
            else:
                start += month
            if start % 7 == 6:
                count += 1
    return count

process()