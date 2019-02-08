# write an algorithm to compute the number of trailing zeros in n factorial

# A trailing zero is created with multiples of 10, 
# and multiples of 10 are created with pairs of 5-multiples and 2-multiples
# it is sufficient to count 5-multiples (i.e. 25 = 5 * 5 = two 5-multiples)

import os

def factorsOf5(i):
    count = 0
    while (i % 5 == 0):
        count = count + 1
        i = i / 5
    return count

def countFactZeros(n):
    count = 0
    for i in range(2, n+1):
        count += factorsOf5(i)
    
    return count

# better way to do

def countFactZerosBetter(n):
    count = 0
    if n < 0:
        return -1
    
    i = 5
    while (n/i > 0):
        count += n / i
        i = i * 5
    return count

if __name__=="__main__":
    n = 19
    print(countFactZerosBetter(n))
