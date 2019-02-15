# implement a function to check if a binary tree is balanced. 
# a tree is balanced if the heights of the two subtrees of any node never differ by more than one

# Solution recursively compute the heights of subtrees of each node

import os
import sys
from binary_tree import BTree, createMinimalBST

# not so efficient O(n log n)
def isTreeBalanced(root):
    if root is None:
        return True
    
    heightDiff = getHeight(root.left) - getHeight(root.right)

    if (abs(heightDiff) > 1):
        return False
    else:
        return isTreeBalanced(root.left) and isTreeBalanced(root.right)


def getHeight(node):
    if node is None:
        return -1
    return max(getHeight(node.left), getHeight(node.right)) + 1

# O(N) solution
def checkHeight(root): # a variation of getHeight where this one checks if subtrees are balanced
    if root is None:
        return -1

    leftheight = checkHeight(root.left)
    if leftheight == (-1 * sys.maxint):
        return leftheight

    rightheight = checkHeight(root.right)
    if rightheight == (-1 * sys.maxint):
        return rightheight

    heightdiff = abs(leftheight - rightheight)

    if heightdiff > 1:
        return -1 * sys.maxint
    else:
        return max(leftheight, rightheight) + 1

def isBalanced(root):
    return checkHeight(root) != (-1 * sys.maxint)

if __name__=="__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree_root = createMinimalBST(array)
    print(isTreeBalanced(tree_root))
    print(isBalanced(tree_root))
