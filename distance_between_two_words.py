''' Given any two words, find the shortest distance (in terms of number of words) between them in the file. 
If the operation will be repeated many times for different pairs of words, can you optimize your solution'''

'''
Brute force: Keep location of word1 and word2 in two variables and keep updating them 
if the distance is shorter than previous one
'''

'''
for repeat queries - we can store a hash map that store word and its locations. 
then finding the shortest distance is to find two numbers in these lists that have the min difference
'''

import os 

# brute force run once
def findClosest(words, word1, word2):
    bestloc = (-1, -1)
    currentloc = (-1, -1)

    for i in range(0, len(words)):
        word = words[i]
        if word == word1:
            currentloc[0] = i
            if abs(i - bestloc[1]) < abs(bestloc[0]-bestloc[1]):
                bestloc[0] = i
        elif word == word2:
            currentloc[1] = i
            if abs(i - bestloc[0]) < abs(bestloc[0] - bestloc[1]):
                bestloc[1] = i
    return bestloc

# hash map solution

def createHashMap(words):
    locations = {}
    for i in range(0, len(words)):
        if words[i] not in locations.keys():
            locations[words[i]] = []
        locations[words[i]].append(i) # this is always inserted in sorted order

    return locations

def findMinDistancePair(locations, word1, word2):
    array1 = locations[word1]
    array2 = locations[word2]

    index1 = 0
    index2 = 0

    bestloc = (0, 0)
    currentloc = (0,0)

    while (index1 < len(array1) and index2 < len(array2)):
        currentloc = (index1, index2)
        if abs(array1[currentloc[0]]-array2[currentloc[1]]) < abs(array1[bestloc[0]]-array2[bestloc[1]]):
            bestloc = currentloc
        if array1[index1] < array2[index2]:
            index1 += 1
        else:
            index2 += 1

    return bestloc

        