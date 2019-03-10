''' Find the kth number whose only prime factors are 3, 5, and 7 '''

''' Solution: create 3 lists to hold multiples of 3, 5, and 7 
    keep taking their min and multiplying that with 3, 5, and 7 and putting the numbers in their appropriate queue
    taking the min value in a variable.
    Do this K times and the final result will be in the min value variable '''

import os
import sys
from collections import deque

def getKthMagicNumber(k):
    if k < 0:
        return 0
    
    val = 0
    Q3 = []
    Q5 = []
    Q7 = []

    Q3.append(1)

    for i in range(0, k):
        
        v3 = Q3[0] if len(Q3) > 0 else sys.maxint
        v5 = Q5[0] if len(Q5) > 0 else sys.maxint
        v7 = Q7[0] if len(Q7) > 0 else sys.maxint

        val = min(v3, min(v5, v7))
        if (val == v3): # enqueue into queue 3, 5, and 7
            Q3.pop(0)
            Q3.append(3*val)
            Q5.append(5*val)
        elif (val == v5): # enqueue into Q5 and Q7
            Q5.pop(0)
            Q5.append(5*val)
        elif (val == v7): # enqueue into Q7
            Q7.pop(0)
        Q7.append(7*val)
    return val


if __name__=="__main__":
    print(getKthMagicNumber(7))