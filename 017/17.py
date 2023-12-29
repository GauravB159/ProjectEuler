from pelib.basic import timed

def getRepresentation(n):
    mapper = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50:"fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand"
    }
    result = {}
    representation = ""
    count = 0
    prev = -1
    for key in list(mapper.keys())[::-1]:
        if not n:
            break
        if n >= key:
            result[key] = n // key
            n = n - (n // key) * key
            if count == 0 and key > 99:
                representation += f"{mapper[result[key]]} {mapper[key]} "
            else:
                representation += f"{mapper[key]} "
            if prev == 100 or (prev == 1000 and key != 100):
                representation += "and "
            prev = key
            count += 1
    
    return representation

@timed
def process():
    answer = 0
    for i in range(1, 1001):
        rep = getRepresentation(i)
        letters = len(rep.replace(" ", ""))
        answer += letters
    return answer

process()