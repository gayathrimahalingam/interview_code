###  Add without plus: Write a function that adds two numbers. You should not use any arithmetic operators

# Solution
# XOR operators adds without carrying
# (a & b) << 1 i.e. (a AND b) (left shift) 1 will produce carry alone
# then set a = sum and b = carry
# repeat this until b is not zero

import os 

def addWithoutPlus(a, b):
    while (b != 0):
        s = a ^ b
        carry = (a & b) << 1
        a = s 
        b = carry

    return a 

if __name__=="__main__":
    a = 10
    b = 24
    print (addWithoutPlus(a,b))
    