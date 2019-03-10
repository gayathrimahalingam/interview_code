''' Given a list of pair of items, find the longest subsequence such that 
both the first and second items are in non-decreasing order '''
''' height weight '''

# Brute force is to try to find all possible sequences

# Optimal and iterative is to see if we can find the longest subsequence that terminates with A[i] for each i

import os

def maximum(seq1, seq2):
    if len(seq1) > len(seq2):
        return seq1
    else:
        return seq2

def canAppend(solution, value):
    if len(solution) == 0:
        return True
    
    last = solution[-1]
    return last < value


def longestIncreasingSeq(array):
    ht_sorted = sorted(array, reverse=True)
    solutions = {}

    for i in range(0, len(array)):
        solutions[i] = []

    bestSequence = []
    # find the longest subsequence that terminates with each element. Track the longest overall subsequence as we go
    for i in range(0, len(array)):
        longestAtIndex = bestSeqAtIndex(array, solutions, i)
        solutions[i] = longestAtIndex
        bestSequence = maximum(bestSequence, longestAtIndex)

    return bestSequence

# find the longest subsequence which terminates with this element
def bestSeqAtIndex(array, solutions, index):
    value = array[index]
    bestSequence = []

    # find the longest subsequence that we can append this element to
    for i in range(0, index):
        solution = solutions[i]
        if canAppend(solution, value):
            bestSequence = maximum(solution, bestSequence)

    best = bestSequence
    best.append(value)
    return best


if __name__=="__main__":
    array = [(1,2), (3,2), (2,4), (5,3), (8,7)]
    seq = longestIncreasingSeq(array)
    print(seq)