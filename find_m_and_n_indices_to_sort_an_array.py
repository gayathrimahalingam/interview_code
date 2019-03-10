# Given an array of integers, write a method to find indices m and n
# such that if you sorted elements m through n, the entire arryay would
# be sorted. Minimize n - m 

import os

def findUnsortedSequence(arr):
    # find the left sorted subsequence
    end_left = findEndOfLeftSubsequence(arr)
    if end_left >= len(arr) - 1: # array is already sorted
        return
    start_right = findStartOfRightSubsequence(arr)
    print(end_left, start_right)

    # find the min and max of arr
    max_index = end_left # max of left side
    min_index = start_right # min of right side

    # find the min and max of the middle
    for i in range(end_left+1, start_right):
        if (arr[i] < arr[min_index]):
            min_index = i
        if (arr[i] > arr[max_index]):
            max_index = i 

    # slide left until less than arr[min_index]
    left_index = shrinkLeft(arr, min_index, end_left)
    right_index = shrinkRight(arr, max_index, start_right)

    return left_index, right_index

def shrinkLeft(arr, min_index, start):
    comp = arr[min_index]
    for i in range(start-1, 0, -1):
        if arr[i] <= comp:
            return i+1
    return 0

def shrinkRight(arr, max_index, start):
    comp = arr[max_index]
    for i in range(start, len(arr)):
        if arr[i] >= comp:
            return i-1
    return len(arr)-1

def findEndOfLeftSubsequence(arr):
    for i in range(1, len(arr)):
        if (arr[i] < arr[i-1]):
            return i-1
    return len(arr)-1

def findStartOfRightSubsequence(arr):
    for i in range(len(arr)-1, 1, -1):
        if (arr[i] < arr[i-1]):
            return i 

if __name__=="__main__":
    arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    left, right = findUnsortedSequence(arr)
    print(left, right)
