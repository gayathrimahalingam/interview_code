''' First common ancestor: Design an algorithm to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure
This is not a binary search tree '''

# Traverse up parent to find the match

import os

def commonAncestor(p, q):
    if p is None or q is None:
        return None

    # find the diff in height of these two nodes
    # there is no chance that they intersect below the shallow depth node
    depthdiff = depth(p) - dept(q)
    
    shallow = q if depthdiff > 0 else p # get shallower node
    deeper = p if depthdiff > 0 else q # get deeper node

    # move up the deeper node to the height of shallow by depthdiff
    deeper = goUpBy(deeper, depthdiff)

    # find where paths intersect
    while ((shallow is not deeper) and (shallow is not None) and (deeper is not None)):
        shallow = shallow.parent
        deeper = deeper.parent

    if ((shallow is None) or (deeper is None)):
        return None
    else:
        return shallow

def goUpBy(node, depth):
    while (depth > 0 and node is not None):
        node = node.parent
        depth -= 1
    return node

def depth(node):
    dep = 0
    while node is not None:
        node = node.parent 
        dep += 1
    return dep



# If parent is not available, we 
# find if one node's parent cover the others and keep going up until it does

def commonAncestorNoParent(root, p, q):
    node, ancestor = commonAncestorNoParentHelper(root, p, q)
    if ancestor:
        return node
    else:
        return None

def commonAncestorNoParentHelper(root, p, q):
    if root is None: 
        return None, False
    
    if root is p or root is q:
        return root, True
    
    rxnode, rxancestor = commonAncestorNoParentHelper(root.left, p, q)
    if rxancestor:
        return rxnode, rxancestor
    
    rynode, ryancestor = commonAncestorNoParentHelper(root.right, p, q)
    if ryancestor:
        return rynode, ryancestor
    
    if (rxnode is not None) and (rynode is not None):
        return 

