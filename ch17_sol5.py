# given an array filled with letters and numbers 
# find the longest subarray with an equal number of letters and numbers

# Solution
# count the number of characters and numbers up until every position in the array 
# compute the difference in the count at each position
# the positions i and j that are farthest apart and have the same difference is the
# longest subarray (the diff will be the same only when equal number of chars and nums are added)

import os

def computeDeltaArray(arr):
    deltas = []
    delta = 0
    for i, a in enumerate(arr):
        if a.isdigit(): # python 3 this is
            delta = delta - 1
        else:
            delta = delta + 1
        deltas.append(delta)
    return deltas

def findLongestMatch(deltas):
    hashmap = {}
    hashmap[0] = -1
    maxstart = 0
    maxend = 0
    for i, d in enumerate(deltas):
        if d not in hashmap.keys():
            hashmap[d] = i
        else:
            match = hashmap[d]
            distance = i - match
            longest = maxend - maxstart
            if longest < distance:
                maxend = i + 1
                maxstart = match + 1

    return maxstart, maxend
    

def findLongestSubarray(arr):
    # compute the difference in #chars and #numbers
    deltas = computeDeltaArray(arr)
    
    # find pair in deltas with matching values and largest span
    maxstart, maxend = findLongestMatch(deltas)

    return arr[maxstart:maxend]

if __name__=="__main__":
    arr = ["a", "a", "a", "a", "1", "1", "a", "1", "1", "a", "a", "1", "a", "a", "1", "a", "a", "a", "a", "a"]
    arr = ["a", "a", "1", "1", "1", "a", "a", "a"]
    print(findLongestSubarray(arr))
