# implement multiply, subtract and divide operations for integers
# use only the add operator

import os 

def negate(num):
    neg = 0
    if num < 0:
        newsign = 1
    else:
        newsign = -1
    
    while (num != 0):
        neg += newsign
        num += newsign

    return neg

def subtract(a, b):
    return a + negate(b)

def multiply(a, b):
    if a < b:
        return(multiply(b, a))
    
    sum = 0
    runner = b
    while (runner > 0):
        sum = sum + a 
        runner = subtract(runner, 1)

    if b < 0:
        sum = negate(sum)
    return sum

def absolute(num):
    if num < 0:
        return negate(num)
    else:
        return num

def division(a, b):
    if (b == 0):
        return -1
        # or throw an exception
    absa = abs(a)
    absb = abs(b)

    product = 0
    numerator = 0
    while (product + absb <= absa):
        product += absb
        numerator += 1

    if ((a < 0 and b < 0) or (a > 0 and b > 0)):
        return numerator
    else:
        return negate(numerator)

