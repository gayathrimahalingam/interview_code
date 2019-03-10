# write a method that finds the maximum of two numbers. 
# You should not use if-else or any other comparison operator

# A negative number in binary has its last bit (left one) as 1
# so we can find
# 1. a - b 
# 2. if a - b >= 0 then k is 1 else k = 0
# 3. let q be inverse of k (i.e. flip(k))

# works only if there is no overflow
# overflow happens when a is positive and b is negative

import os 

def flip(bit):
    return 1 ^ bit

def sign(a):
    return flip((a >> 31) & 1)

def findMax(a, b):
    k = sign(a - b) 
    q = flip(k)
    return a * k + b * q


def getMax(a, b):
    c = a - b 

    sa = sign(a) # if a >= 0 then 1 else 0
    sb = sign(b) # if b >= 0 then 1 else 0
    sc = sign(c) # depends on whether or not a - b overflows

    use_sign_of_a = sa ^ sb
    use_sign_of_c = flip(sa ^ sb)

    k = use_sign_of_a * sa + use_sign_of_c * sc
    q = flip(k)
    return a * k + b * q


if __name__=="__main__":
    a = 15
    b = 24
    print(findMax(a,b))