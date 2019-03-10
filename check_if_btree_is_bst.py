# Implement a function to check if a binary tree is a valid binary search tree

# BST - left <= root < right
# An in-order traversal array should be sorted 
# recursively check if BST property is maintained

# more optimal: have a min and max variable and check while you traverse to get a O(N) solution

import os

def isValidBST(root):
    return checkValidBST(root, None, None)

def checkValidBST(root, mins, maxes):
    if root is None:
        return True
    
    if (((mins is not None) and root.data <= mins) or ((maxes is not None) and root.data > maxes)):
        return False
    
    if (not(checkValidBST(root.left, mins, root.data) or not(checkValidBST(root.right, root.data, maxes)))):
        return False
    
    return True
    