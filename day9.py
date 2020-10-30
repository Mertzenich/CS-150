#!/usr/bin/env python3

import math

# Palindrome Checker from Problem 8
def palCheck(w):
    if w == w[len(w)::-1]:
        return True
    return False

# Problem 1-4

ls = [3, 9, 2, 1, 10]

listSum = sum(ls)
print(listSum)                  # Problem 1

listMult = math.prod(ls)
print(listMult)                 # Problem 2

ls.sort()
print(ls[-1])                   # Problem 3
print(ls[0])                    # Problem 4


# Problem 5

def firstLastCounter(sampleList):
    for i in sampleList:
        if len(i) < 2:          # Remove items that are too small
            sampleList.remove(i)

    fl = []
    for i in sampleList:
        if i[0] is i[-1]:
            fl.append(i)
    return len(fl)

print(firstLastCounter(['abc', 'xyz', 'aba', '1221']))

# Problem 6
def duplicateRemover(start):
    new = []

    for i in start:
        if i not in new:
            new.append(i)

    return new

start = ['abc', '1221', 'xyz', 'aba', '1221', 'xyz']

print(duplicateRemover(start))
