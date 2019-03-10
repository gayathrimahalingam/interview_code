''' BiNode has two pointers to two other nodes. Convert binary search tree to doubly linked list 
the values should be kept in order and the operation should be performed in place '''

# Solution: Recursively perform inorder traversal

import os 

class BiNode():
    def __init__(self):
        self.data = None
        self.node1 = None
        self.node2 = None
    

# O(N^2) runtime
def convertToLL(root):
    if root is None:
        return None

    left = convert(root.node1)
    right = convert(root.node2)

    if left is not None:
        concat(getTail(left), root)

    if right is not None:
        concat(getTail(right), root)

    if left is None:
        return root
    else:
        return left

def getTail(node):
    if node is None:
        return None
    while node.node2 is not None:
        node = node.node2
    return node

# build a circular linked list
# O(N) runtime

def convertToCircular(root):
    if root is None:
        return None

    part1 = converToCircular(root.node1)
    part3 = converToCircular(root.node2)

    if part1 is None and part3 is None:
        root.node1 = root
        root.node2 = root
        return root
    
    if part3 is None:
        tail3 = None
    else:
        tail3 = part3.node1
    
    # join left to root
    if part1 is None:
        concat(part3.node1, root)
    else:
        concat(part1.node1, root)

    # join right to root
    if part3 is None:
        concat(root, part1)
    else:
        concat(root, part3)

    # join right to left
    if part1 is not None and part3 is not None:
        concat(tail3, part1)
    
    if part1 is None:
        return root
    else:
        return part1

def convert(root):
    head = convertToCircular(root)
    head.node1.node2 = None
    head.node1 = None
    return head
    
