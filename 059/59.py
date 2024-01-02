from pelib.basic import timed

def encrypt(input, key):
    for i in range(len(input)):
        input[i] = input[i] ^ key[i % len(key)]
    return input

@timed
def process():
    text = open("input.txt").read().split(",")
    text = [int(x) for x in text]
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            for k in range(ord('a'), ord('z') + 1):
                encrypt(text, [i, j, k])
                output = ''.join([chr(i) for i in text])
                if ' the ' in output:
                    return sum(text)
                encrypt(text, [i, j, k])

process()