# smallest difference: 
# given two arrays of integers, compute the pair of values (one value from each array)
# with the smallest (non-negative) difference.

# key is to sort the arrays and have ptrs for each array and find the pair that gives the smallest diff

import os
import sys

def smallestDiff(a, b):
    a.sort()
    b.sort()
    mindiff = sys.maxint

    i = 0
    j = 0

    while (i < len(a) and j < len(b)):
        if (abs(a[i]-b[j]) < mindiff):
            mindiff = abs(a[i]-b[j])
        
        # move the ptr to the smallest so that their diff gets smaller
        if a[i] < b[j]:
            i = i + 1
        else:
            j = j + 1
    return mindiff

if __name__=="__main__":
    a = [1,2,11,15]
    b = [4,12,19,23,127,235]
    print(smallestDiff(a,b))
