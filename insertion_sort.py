### insertion sort

import os

def insertionSort(llist):
    for j in range(1, len(llist)):
        key = llist[j]
        i = j-1
        while i >= 0 and llist[i] > key: # for non-increasing llist[i] < key
            llist[i+1] = llist[i]
            i = i - 1
        llist[i+1] = key


if __name__=="__main__":
    A = [5, 2, 4, 6, 1, 3]
    insertionSort(A)
    print(A)