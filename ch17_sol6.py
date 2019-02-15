# count the number of 2s between 0 and n

# brute force is to go through every number and count the number of 2s in its digit
# optimal solution is to look at each digit (d) and check if d < 0 or d > 1 or d == 2
# if d < 2, then #2s: y = round down to nearest 10^(d+1) and return y /10
# if d > 2, then #2s: y = round up to nearest 10^(d+1) and return y / 10
# if d = 2, then #2s: y = round down to nearest 10^(d+1) and return y/10 + (num % 10^d)
# num % 10^d is the remainder of times digit d stays 2 (e.g. between 62000 - 62543, it is 543)

import os

def countTwosInDigit(number, digitpos):
    powerof10 = 10**digitpos
    nextpowerof10 = powerof10 * 10
    right = number % powerof10

    roundDown = number - (number % nextpowerof10)
    roundup = roundDown + nextpowerof10

    digit = (number / powerof10) % 10
    if (digit < 2):
        return roundDown / 10
    elif (digit > 2):
        return roundup / 10
    elif (digit == 2):
        return (roundDown / 10) + right + 1

def countTwosInNumber(number):
    count = 0
    for i in range(0, len(str(number))):
        count = count + countTwosInDigit(number, i)
    return count

def bruteforce(number):
    count = 0
    for i in range(2, number+1):
        count = count + numberof2s(i)
    return count

def numberof2s(num):
    c = 0
    while (num > 0):
        if (num % 10 == 2):
            c = c + 1
        num = num / 10
    return c

if __name__=="__main__":
    number = 2020
    print(countTwosInNumber(number))
    print(bruteforce(number))