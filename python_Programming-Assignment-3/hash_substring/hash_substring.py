# python3
from random import randint
# import argparse
def RabinKarp(text, pattern):
    p = 2000001
    x = randint(1, p - 1)
    result = []
    patternHash = PolyHash(pattern, p, x)
    hashes = PrecomputeHashes(text, pattern, p, x)
    for i in range(0, len(text) - len(pattern) + 1):
        if (patternHash == hashes[i] and pattern == text[i : (i + len(pattern))]):
            result.append(i)
    return result


def PolyHash(Pattern, p, x):
    hash = 0
    for char in reversed(Pattern):
        hash = ((hash * x) + ord(char)) % p
    return hash

def PrecomputeHashes(text, pattern, p, x):
    hashes = [0 for i in range(0, len(text) - len(pattern) + 1)]
    startingIndex = len(text) - len(pattern)
    lastString = text[startingIndex:]
    hashes[-1] = PolyHash(lastString, p, x)
    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
    for i in reversed(range(0, (len(text) - len(pattern)))):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - (y * ord(text[i + len(pattern)]))) % p
    return hashes

def read_input():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("filename", help="The filename to be processed")
    # args = parser.parse_args()
    # lines = list()
    # if args.filename:
    #     with open(args.filename) as f:
    #         for line in f:
    #                 lines.append(line)
    # return (lines[0].rstrip(), lines[1].rstrip())
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return RabinKarp(text, pattern)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

