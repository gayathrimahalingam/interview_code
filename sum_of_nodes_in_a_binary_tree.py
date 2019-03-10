# given the binary tree, go through the tree and return sum of nodes in the tree

import os

# solution 1: find sum of subtrees and add the root's value to it

def sumBTree(root):
    if root is None:
        return 0
    s = sumBTree(root.left) + root.value + sumBTree(root.right)
    return s 

