# given a sorted array with unique integer elements, write an algorithm to create a binary search tree with minimal height

# solution: insert middle element recursively to make a minimal height tree

import os 


class Node():
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None 

    def getNodeValue(self):
        return self.value


def createMinimalBST(array):
    return createMinimalBSTree(array, 0, len(array)-1)

def createMinimalBSTree(array, start, end):
    if end < start:
        return None
    
    mid = (start + end) / 2
    n = Node(array[mid])
    n.left = createMinimalBSTree(array, start, mid-1)
    n.right = createMinimalBSTree(array, mid+1, end)
    return n

def printTree(root):
    if root is None:
        return
    elif root.left is None and root.right is None:
        print(root.value)
        return
    else:
        print(root.value)
        printTree(root.left)
        printTree(root.right)
        return
        

if __name__=="__main__":
    array = [1,2, 3, 4, 5, 6, 7, 8, 9]
    node = createMinimalBST(array)
    printTree(node)