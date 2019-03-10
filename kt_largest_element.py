''' kth largest / smallest element 

Solution: selection rank algorithm (if you can modify the original array)
Solution: Red Black trees with rank in each node specified
'''

import os
import random
from binary_tree import *

# based on quicksort method O(N) but array need to have distinct elements

def randomNum(lower, higher):
    return random.randint(lower, higher)

def partition(array, left, right, pivot):
    while (True):
        # find the first element that is greater than the pivot
        while (left <= right and array[left] <= pivot):
            left += 1
        # find the first element in the right that is lesser than the pivot
        while (left <= right and array[right] > pivot):
            right -= 1
        
        if (left > right):
            return left - 1
        swap(a, left, right)
        left += 1
        right -= 1


def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

def rank(array, left, right, ranks):
    randnum = randomNum(left, right)
    pivot = array[randnum]

    # partition and return end of left partition
    leftEnd = partition(array, left, right, pivot)

    leftSize = leftEnd - left + 1
    if leftSize == ranks + 1:
        return max(a[left], a[leftEnd])
    elif ranks < leftSize:
        return rank(a, left, leftEnd, ranks)
    else:
        return rank(a, leftEnd+1, right, ranks-leftSize)


''' kth largest element in a BST '''

def kthLargestHelper(root, k, count):
    if root is None or count[0] >= k:
        return

    # follow right to find the kth largest
    # follow left to find the kth smallest
    kthLargestHelper(root.right, k, count) 
    count[0] += 1
    
    if count[0] == k:
        print(root.data)
        return
    
    kthLargestHelper(root.left, k, count)

def kthLargestElement(root, k):
    count = [0]
    kthLargestHelper(root, k, count)

''' kth smallest element in a BST '''
def kthSmallestHelper(root, k, count):
    if root is None or count[0] >= k:
        return

    kthSmallestHelper(root.left, k, count)
    count[0] += 1

    if count[0] == k:
        print(root.data)
        return
    
    kthSmallestHelper(root.right, k, count)

def kthSmallestElement(root, k):
    count = [0]
    kthSmallestHelper(root, k, count)

if __name__=="__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    tree_root = createMinimalBST(array)
    #printTree(tree_root)
    kthLargestElement(tree_root, 4)
    kthSmallestElement(tree_root, 4)



    