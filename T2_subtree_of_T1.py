''' check if T2 is a subtree of T1 

Solution 1: get an in order traversal of T1 and T2 and check if T2 is a subarray of T1

Solution 2: traverse T1 and check if any of its subtrees is like T2
'''

import os

def subTree(t1, t2):
    if t1 is None:
        return False
    
    if t1.data == t2.data:
        if matchTree(t1, t2):
            return True
    
    return (subTree(t1.left, t2) or subTree(t1.right, t2))

def matchTree(t1, t2):
    if t1 is None and t2 is None:
        return True # both trees are empty and hence equal
    # if one but not both are empty
    if t1 is None or t2 is None:
        return False
    
    if t1.data != t2.data:
        return False
    
    return (matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right))

def T2_subtree_T1(t1, t2):
    if t2 is None:
        return True # empty tree is always a subtree
    else:
        return subTree(t1, t2)
