''' find all nodes at height k from leaf node '''

import os

def kNodesFromLeaf(root, k):
    if root in None:
        return None
    
    kNodesFromLeaf(root.left, k)
    kNodesFromLeaf(root.right, k)

    leftheight = findheight(root.left)
    rightheight = findheight(root.right)

    ht = max(leftheight, rightheight) + 1

    if ht == k:
        return root

def findheight(node):
    if node is None:
        return -1
    
    if node.left is None and node.right is None: # leaf node
        return 0
    
    return max(findheight(node.left), findheight(node.right)) + 1
