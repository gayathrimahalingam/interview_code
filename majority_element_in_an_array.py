''' A majority element is an element that makes up more than half of the items in an array
Given a positive integers array, find the majority element. 
If there is no majority element return -1.
Do this in O(N) time and O(1) space '''


'''
Solution: start with first element and expand that subarray until this element is no lonfer the majority element
e.g. start with [3] and then add next element [3, 1] -> this has no majority for 3... so we fail
then we start with element after 1 in [3,1] and repeat the same... 
Keep doing this until you find a subarray with a majority element.
then we should validate this majority element
'''

'''
Another solution is to use hash map 
'''

''' A similar problem is 
given an array of 2n elements of which n elements are same and the remaining are all different.
Find the value which is present n times in the array '''

import os 

# if elements are within a range then keep adding range k to arr with index arr[i]%k
# the most repeating element will have more range added to it
# return the index of max element 
# you can mod back to return the original value

def max_repeating(arr, range):
    for i in range(len(arr)):
        arr[arr[i]%range] += range
    
    maxi = arr[0]
    index = i
    for i in range(1, len(arr)):
        if (maxi < arr[i]):
            maxi = arr[i]%range
            result = i 
    return maxi, result

# brute force
def findMajority(arr):
    n = len(arr)

    maxcount = 0
    index = -1
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        if count > maxcount:
            maxcount = count
            index = i

    if (maxcount > n/2):
        return arr[index]
    else:
        return -1


# optimized (Moore's voting method - works if there is a majority element)
def findMajorityElement(array):
    candidate = getCandidate(array)
    if validate(array, candidate):
        return candidate
    else:
        return -1


def getCandidate(array):
    majority = 0
    count = 0
    for n in array:
        if count == 0:
            majority = n
        if n == majority:
            count = count + 1
        else:
            count = count - 1
    return majority

def validate(array, candidate):
    count = 0
    for n in array:
        if n == candidate:
            count = count + 1

    if count > (len(array) / 2):
        return True
    else:
        return False

if __name__=="__main__":
    array = [7, 3, 7, 1, 7, 1, 7, 3, 7, 3, 7]
    print(findMajorityElement(array))
    print(findMajority(array))