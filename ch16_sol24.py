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


if __name__=="__main__":
    arr = [-2, -1, 0, 3, 5, 6, 7, 9, 13, 14]
    getPairSum(arr, 8)
        