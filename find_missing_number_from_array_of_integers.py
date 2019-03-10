# find the missing number from an array of integers from 0 to n

# look at every bit of the numbers in the array

import os

def bit_length(n):
    c = 0
    newn = n
    while (newn > 0):
        newn = newn >> 1
        c = c + 1
    return c

def countZerosAndOnesFromLSB(arr, bitnum):
    zeros = 0
    ones = 0
    for a in arr:
        if a & (1 << bitnum) > 0:
            ones = ones + 1
        else:
            zeros = zeros + 1
    return zeros, ones


def findMissingInteger(arr, n):
    missing = 0
    bitlen = bit_length(n)
    newarr = arr
    missingBits = []
    for i in range(0, bitlen):
        #print(newarr)
        zeros, ones = countZerosAndOnesFromLSB(newarr, i)
        #print(i, zeros, ones)
        if zeros <= ones:
            # LSB(missingnum) is 0 so missingnum is even
            missingBits.append(0)
            missing = missing + 0
            # remove all odd numbers from arr
            newarr = [m for m in newarr if ((m & (1<<i))>>i)==0]
        elif zeros > ones:
            # LSB(missingnum) is 1 so missingnum is odd
            missingBits.append(1)
            missing = missing + 2**i
            # remove all even numbers from arr
            newarr = [m for m in newarr if ((m & (1<<i))>>i)==1]
        #print(missingBits)
    return missing

if __name__=="__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]
    n = 8
    print(findMissingInteger(arr, n))

