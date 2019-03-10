''' 
Shortest Supersequence: You are given two arrays, one shorter (with all distinct elements) and one
longer. Find the shortest subarray in the longer array that contains all the elements in the shorter
array. The items can appear in any order.

EXAMPLE
Input:
{1, 5, 9}
{7, 5, 9, 0, 2, 1, 3, 5. 7, 9. 1, 1, 5, 8, 8, 9, 7}
Output:[7, 10] (the underlined portion above)

'''

'''
Solution
Find the index of occurences of each small element and put them in individual arrays
the sub-array indices will be to min of the first elements - max of the first elements
remove the min and repeatedly find the min - max lengths 
return the shortest
'''

# PROBLEM INCOMPLETELY CODED

import os 
import numpy as np


def shortestSuperSequence(bigarray, smallarray):
    index_occurences = get_index_occurences(bigarray, smallarray)

    best_min_range = -1
    best_max_range = -1
    best_length = 0
    # extract the head elements from these
    min_head = get_min(index_occurences)

def get_index_occurences(big, small):
    indices = []
    for s in small:
        indices[s] = []

    for s in small:
        indices[s] = get_all_occurences(big, s)

    return indices

def get_all_occurences(big, s):
    index = []

    for i, b in enumerate(big):
        if b == s:
            index.append(i)

    return index

def get_min(indexes):
    heads = [(i[0], a) for a, i in enumerate(indexes) if len(i) > 0]
    heads = np.array(heads)

    mins = np.amin(heads, axis=0)[0]
    maxs = np.amax(heads, axis=0)[0]
    

