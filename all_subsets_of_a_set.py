''' Generate all the subsets of a set '''

import os
import math

def powerset(set, set_size):
    pow_set_size = int(math.pow(2, set_size))
    counter = 0
    j = 0

    allsubsets = []
    # run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        subset = []
        for j in range(0, set_size):
            # check if jth bit in the counter is set
            # if set thenn print the jth element from set
            if ((counter & (1 << j)) > 0):
                print(set[j], end="")
                subset.append(set[j])
        allsubsets.append(subset)
        print("")


if __name__=="__main__":
    array = [1,2,3]
    allsubsets = powerset(array, len(array))