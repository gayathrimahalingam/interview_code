''' Wite an algorithm to find the next node in-order successor of a given node in a binary search
tree. You may assume that each node has a link to its parent '''

'''
if node has right subtree, then return leftmost child of right subtree
if not, go up tracing parent until the parent is a left child to its parent
then return that parent '''

import os

def inOrderSuccessor(node):
    if node is None:
        return None
    
    if node.right is not None:
        return leftmostChild(node.right)
    else:
        q = node
        p = q.parent

        while ((p is not None) and (p.left is not q)):
            q = p
            p = q.parent
        return p

def leftmostChild(node):
    if node is None:
        return None
    while (node.left is not None):
        node = node.left
    return node


