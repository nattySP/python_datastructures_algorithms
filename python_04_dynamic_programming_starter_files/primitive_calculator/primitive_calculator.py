# python3
import sys
import math

def optimal_sequence(n):
    minSequence = [[] for i in range(0, n + 1)]
    minSequence[1] = [1]
    ops = [1, 2, 3]

    for m in range(2, n + 1):
        minNumOps = math.inf
        for op in ops:
            if m >= op:
                if op == 1:
                    prevIndex = m - 1
                    lastNumber = minSequence[prevIndex][-1]
                    newSequence = minSequence[prevIndex][:]
                    newSequence.append(lastNumber + 1)
                    if len(newSequence) <= minNumOps:
                        minSequence[m] = newSequence
                        minNumOps = len(newSequence)
                if op == 2 and m % 2 == 0:
                    prevIndex = m // 2
                    lastNumber = minSequence[prevIndex][-1]
                    newSequence = minSequence[prevIndex][:]
                    newSequence.append(lastNumber * 2)
                    if len(newSequence) <= minNumOps:
                        minSequence[m] = newSequence
                        minNumOps = len(newSequence)
                if op == 3 and m % 3 == 0:
                    prevIndex = m // 3
                    lastNumber = minSequence[prevIndex][-1]
                    newSequence = minSequence[prevIndex][:]
                    newSequence.append(lastNumber * 3)
                    if len(newSequence) <= minNumOps:
                        minSequence[m] = newSequence
                        minNumOps = len(newSequence)

    return minSequence[n]

input = sys.stdin.read()
# input = '96234'
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
