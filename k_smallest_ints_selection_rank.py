''' find the k smallest integers froma given array'''

'''
Solution 1: Sort the array and return the first k elements
Solution 2: Use a BST and do in order traversal to find first k elements
Solution 3: Selection rank algorithm

Selection Rank
1. Pickarandomelementinthearrayanduseitasa"pivot:'Partitionelementsaroundthepivot,keeping
track of the number of elements on the left side of the partition.
2. Ifthereareexactlyielementsontheleft,thenyoujustreturnthebiggestelementontheleft.
3. Ifthele sideisbiggerthani,repeatthealgorithmonjustthele partofthearray.
4. Iftheleftsideissmallerthani,repeatthealgorithmontheright,butlookfortheelementwithrank
i - leftSize.
'''

import os 
import random

def smallestK(array, k):
    if k <= 0 or k > len(array):
        return None
    
    # get an item with rank k-1
    threshold = rank(array, k-1)

    # copy elements smaller than the threshold
    smallest = []
    count = 0
    for a in array:
        # copy elements that are only smaller than threshold
        # prevents filling up smallest with duplicates
        if a < threshold and count < k:
            smallest.append(a)
            count += 1

    return smallest

# find a value in array with rank k
def rank(array, k):
    if k >= len(array):
        return -1
    return rankHelper(array, k, 0, len(array)-1)


def randomNum(lower, higher):
    return random.randint(lower, higher)

def partition(array, start, end, pivot):
    left = start
    right = end
    middle = start 
    while (middle <= right):
        if (array[middle] < pivot):
            # middle is smaller than pivot
            # left is either small or equal to pivot
            # so swap middle and left
            swap(array, middle, left)
            middle += 1
            left += 1
        elif (array[middle] > pivot):
            # swap middle with right
            swap(array, middle, right)
            right -= 1
        elif array[middle] == pivot:
            # middle is equal to pivot move to next middle
            middle += 1
    # return sizes of left and middle
    return (left-start, right-left+1)


def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp


# Find value with rank k in sub array between start and end.
def rankHelper(array, k, start, end):
    # partition array around a pivot
    randnum = randomNum(start, end)
    pivot = array[randnum]
    
    # partition the array
    leftSize, middleSize = partition(array, start, end, pivot)

    if (k < leftSize):
        # rank k is on left half
        return rankHelper(array, k, start, start+leftSize-1)
    elif (k < leftSize+middleSize): 
        # rank k is in the middle
        return pivot # middle is all pivot values
    else:
        # rank k is on the right
        return rankHelper(array, k-leftSize-middleSize, start+leftSize+middleSize, end)
