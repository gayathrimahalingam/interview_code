# design an algorithm to find all pairs of integers within an array which sum to a specified value

# use hash to store the array and search for the diff

def getPairSum(arr, sums):
    hasharr = {}
    for a in arr:
        hasharr[a] = a 
    
    for a in arr:
        complement = sums - a 
        if complement in hasharr.keys():
            print(a, complement)

# sort the array and have two pointer one at start and other at end to find the pair that match the sum

def getsumpair(arr, sums):
    arr.sort()
    newarr = arr
    first = 0
    last = len(newarr)-1

    while (first < last):
        s = newarr[first] + newarr[last]
        if s == sums:
            print(newarr[first], newarr[last])
            first += 1
            last -= 1
        else:
            if s < sums:
                first += 1
            else:
                last -= 1


if __name__=="__main__":
    arr = [-2, -1, 0, 3, 5, 6, 7, 9, 13, 14]
    getPairSum(arr, 8)
    getsumpair(arr, 8)
        