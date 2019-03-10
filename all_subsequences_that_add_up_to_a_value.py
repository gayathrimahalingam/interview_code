''' given an array of number and a value, find all subsequences that add up to that value '''
# NP complete problem Subset sum
# Dynamic programming can also be used

import os
import numpy as np

def isSubsetSumDP(array, sum):
    n = len(array)
    
    # The value of subset[i][j] will be true if there is a subset of array[0..j-1] with sum equal to i
    subset = np.zeros((sum+1, n+1), dtype=bool)

    # if sum is 0, then answer is true
    subset[0][i] = True for i in range(n+1)
    
    # if sum is not 0, and array is empty, then answer is false
    subset[i][0] = False for i in range(1, sum+1)

    # fill the subset table in bottom up manner
    for i in range(1, sum+1):
        for j in range(1, n+1):
            subset[i][j] = subset[i][j-1]
            if i >= array[j-1]:
                subset[i][j] = subset[i][j] or subset[j-1][j-1]

    return subset[sum][n]

# recursive solution

def isSubsetSumRecursive(array, sums):
    n = len(array)
    if sums == 0:
        return True
    if len(array) == 0 and sums != 0)
        return False

    # if last element is greater than sum, then ignore it
    if (array[n-1] > sums):
        return isSubsetSumRecursive(array[0:n-2], sums)

    # else check if sum can be obtained by any of the following
    # 1. including the last element
    # 2. excluding the last element
    return isSubsetSumRecursive(array[0:n-2], sums) or isSubsetSumRecursive(array[0:n-2], sums-array[n-1])
