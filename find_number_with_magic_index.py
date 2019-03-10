# Find the number with magic index i.e. a[i] = i

# brute force is to go through array once to check if a[i] = i
# or do something like quick sort (taking mid and then checking left or right)

import os 
import math

def magicIndex(array, start, end):
    # chck bounds
    if (end < start or start < 0 or end > len(array)):
        return -1

    mid = math.ceil((start+end)/2)
    midval = array[mid]
    
    if mid == midval:
        return mid
    
    # search left
    left = min(mid-1, midval) # handles duplicates
    leftval = magicIndex(array, start, left)
    if leftval >= 0:
        return leftval
    
    # search right
    rightstart = min(mid+1, midval)
    rightval = magicIndex(array, rightstart, end)
    
    return rightval

if __name__=="__main__":
    array = [1, 1, 2, 8, 4, 5, 6]
    print(magicIndex(array, 0, len(array)))
