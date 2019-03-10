# write a method to shuffle a deck of cards. It must be a perfect shuffle. 
# i.e. each of the 52! permutations must be equally likely.

# the cards are in an array, if we can shuffle n-1 element array then
# we can shuffle n element array by randomly picking a k in (0, n-1) and then exchange with n

import os
import random

def shuffleArrayRecursively(cards, i):
    if i == 0:
        return cards
    k = random.randint(0, i)

    # swap k an i th element
    temp = cards[k]
    cards[k] = cards[i]
    cards[i] = temp

    return cards

def shuffleArrayIteratively(cards):
    for i in range(0, len(cards)):
        k = random.randint(0, i)
        # swap k and i
        temp = cards[k]
        cards[k] = cards[i]
        cards[i] = temp

    return cards

if __name__=="__main__":
    cards = range(0, 10)
    print(cards)
    newcards = shuffleArrayIteratively(cards)
    print(newcards)