
### Write a function to swap a number in place (that is without temporary variables)

import os 

def swapInPlace(a, b):
    a = a - b
    b = a + b 
    a = b - a
    return a, b

def swapInPlaceBits(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

if __name__ == "__main__":
    a = 5
    b = 6
    a, b = swapInPlace(a,b)
    print(a, b)
    a, b = swapInPlaceBits(a, b)
    print(a, b)