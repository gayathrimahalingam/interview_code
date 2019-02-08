### peaks and valleys 
# sort an input array into an alternating sequence of peaks and valleys

import os 
import sys

def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

# Approach One:
# Sort the array and swap every element with its right neighbor starting index 1 and increment 2
def peaksAndValleys(arr):
    arr.sort()

    for i in range(1, len(arr), 2):
        swap(arr, i-1, i)

# Approach two:
# No sorting required.
# Place the peaks in their appropriate place so that valleys are automatically in their place

def sortValleyPeak(arr):
    for i in range(1, len(arr), 2):
        biggestIndex = maxIndex(arr, i-1, i, i+1)
        if i != biggestIndex:
            swap(arr, i, biggestIndex)


def maxIndex(arr, a, b, c):
    l = len(arr)
    aValue = -1 * sys.maxint
    bValue = -1 * sys.maxint
    cValue = -1 * sys.maxint
    if a >= 0 and a < l:
        aValue = arr[a]
    if b >= 0 and b < l:
        bValue = arr[b]
    if c >= 0 and c < l:
        cValue = arr[c]
    
    maxValue = max(aValue, max(bValue, cValue))
    if maxValue == aValue:
        return a 
    elif maxValue == bValue:
        return b 
    else:
        return c 

if __name__=="__main__":
    arr = [9, 1, 0, 4, 8, 7]

    peaksAndValleys(arr)
    print(arr)

    sortValleyPeak(arr)
    print(arr)
        