''' find all nodes at height k from root'''

import os

def levelTraversal(root, k):
    if root is None:
        return None
    if k == 0:
        return root
    else:
        levelTraversal(root.left, k-1)
        levelTraversal(root.right, k-1)
