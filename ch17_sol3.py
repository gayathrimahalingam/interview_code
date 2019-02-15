# write a method to randomly generate a set of m integers from an array of size n
# with equal probability

# randomly pick a k from 0 through n. If k < m then swap k with n

import os
import random


def pickIteratively(original, m):
    subset = original[0:m]

    for i in range(m, len(original)):
        k = random.randint(0, i)
        if (k < m):
            subset[k] = original[i]

    return subset

def pickRecursively(original, m, i):
    if i + 1 == m:
        return original[0:m]
    elif i+1 > m:
        subset = pickRecursively(original, m, i-1)
        k = random.randint(0, i)
        if k < m:
            subset[k] = original[i]
        return subset
    return None

if __name__=="__main__":
    original = range(0, 10)
    print(pickIteratively(original, 4))
    print(pickRecursively(original, 4, len(original)-1))