from pelib.basic import getPrimes, timed

def getTemplates():
    templates = []
    def recurse(string):
        if len(string) > 5:
            if "*" in string:
                templates.append(string)
            return
        
        for i in range(10):
            recurse(string + str(i))
        recurse(string + "*")
    recurse("")
    return templates

@timed
def process():
    primes = {x: True for x in getPrimes(1000000)}
    templates = getTemplates()
    for template in templates:
        count = 0
        found = []
        for i in range(10):
            num = int(template.replace("*", str(i)))
            if num in primes:
                if i == 0 and template[0] == '*':
                    break
                count += 1
                found.append(num)
        if len(found) != len(set(found)):
            continue
        if count == 8:
            return found[0]
process()