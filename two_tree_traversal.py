# two tree traversal of two binary trees

import os
from binary_tree import *


def twoTreeTraversal(node1, node2):
    if node1 is None:
        result = node2.inOrderTraversal(node2)
        print(result)
        return
    
    if node2 is None:
        result = node1.inOrderTraversal(node1)
        print(result)
        return
    
    s1 = [] # stack 1
    s2 = [] # stack 2
    c1 = node1
    c2 = node2
    done = False
    flag = False

    while (not done):
        if c1 is not None:
            s1.append(c1)
            c1 = c1.left
        else:
            if (len(s1) == 0 and len(s2) == 0 and c2 is None):
                done = True
            elif len(s1) > 0:
                c1 = s1.pop()
                print c1.data
                flag = True
                c1 = c1.right
        if c2 is not None:
            s2.append(c2)
            c2 = c2.left
        else:
            if (len(s1) == 0 and len(s2) == 0 and c1 is None):
                done = True
            elif len(s2) > 0 and flag is True:
                c2 = s2.pop()
                print(c2.data)
                flag = False
                c2 = c2.right
                
        