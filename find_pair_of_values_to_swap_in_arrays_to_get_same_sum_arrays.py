## given two arrays of integers, find a pair of values (one value from each array) that you 
# can swap to give the two arrays the same sum

import os

# the key is to find an a from A and b from B such that
# sumA - a + b = sumB - b + a
# or a -b = (sumA - sumB) / 2

# this solution assumes that the arrays are sorted
# non sorted arrays solution involves a hash map for the second array

def getTarget(A, B):
    sum1 = 0
    for a in A:
        sum1 = sum1 + a
    sum2 = 0
    for b in B:
        sum2 = sum2 + b 

    if ((sum1-sum2) % 2 != 0):
        return None
    return (sum1-sum2) / 2

def findSwapValues(A, B):
    if len(A) == 0 or len(B) == 0:
        return None
    else:
        target = getTarget(A, B)
        ptra = 0
        ptrb = 0
        while (ptra < len(A) and ptrb < len(B)):
            a = A[ptra]
            b = B[ptrb]
            diff = a - b 
            if (diff == target):
                return (a, b)
            elif (diff < target):
                a = a + 1
            else:
                b = b + 1

        return None

def findSwapValuesWithHash(A, B):
    if len(A) == 0 or len(B) == 0:
        return None
    else:
        target = getTarget(A, B)
        # set the hash map for array B
        bhash = {}
        for b in B:
            bhash[b] = b 
        
        # for each a in A compute a - target and check if that is bhash
        for a in A:
            if ((a-target) in bhash.keys()):
                return (a, bhash[a-target])
        return None

if __name__=="__main__":
    A = [1, 4, 2, 1, 1, 2]
    B = [3, 6, 3, 3]
    print(findSwapValuesWithHash(A, B))