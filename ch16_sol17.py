# you are given an array of integers (both +ve and -ve). Find the contiguous sequence with the largest sum

# idea is to sum up subsequences of positive and negative numbers
# example: (2, 3, -8, -1, 2, 4, -2, 3)'s sum array is (5, -9, 6, -2, 3)
# now examine this array from first element
# 1. take 5 as maxSum and sum. 
# 2. now add -9 to sum. If sum > maxSum then set maxSum to sum, else reset sum

import os

def getMaxSum(arr):
    maxSum = 0
    sums = 0
    for i in range(0, len(arr)):
        sums = sums + arr[i]
        if (maxSum < sums):
            maxSum = sums 
        elif (sums < 0):
            sums = 0
    return maxSum

if __name__=="__main__":
    arr = [2, 3, -8, -1, 2, 4, -2, 3]
    print(getMaxSum(arr))      