# Compute all permutations of a string


import os

def permutation(lst):
    if len(lst) == 1:
        return [lst]
    
    # find the permutations for 1st if there are more than 1 char

    l = [] # empty list to store current permutation

    for i in range(len(lst)):
        first = lst[i]
        remainder = lst[:i] + lst[i+1:]

        for p in permutation(remainder):
            l.append([first] + p)
    return l 
 


if __name__=="__main__":
    str = "apple"
    arr = ["a", "p", "p", "l", "e"]
    perms = permutation(arr)
    for p in perms:
        print(p)