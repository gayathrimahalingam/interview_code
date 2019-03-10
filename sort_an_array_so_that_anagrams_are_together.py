### Write a method to sort an array of strings so that the anagrams are together

import os 

# Time Complexity: Let there be N words and each word has maximum M characters. 
# The upper bound is O(NMLogM + MNLogN).
def sortForAnagrams(arr):
    hashmap = {}

    for i in range(len(arr)):

        # convert to char array and sort the string
        word = arr[i]
        newword = ''.join(sorted(word))

        if newword not in hashmap.keys():
            hashmap[newword] = []
        
        hashmap[newword].append(i)

    newarray = []
    for m in hashmap:
        [newarray.append(arr[i]) for i in hashmap[m]]
    return newarray

# solution using a trie data structure


if __name__=="__main__":
    arr = ["cat", "dog", "tac", "god", "act"]
    newarray = sortForAnagrams(arr)
    print(newarray)