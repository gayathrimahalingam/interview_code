''' Given a binary search tree with distinct elements,
print all possible arrays that could have led to this tree
'''

import os
from binary_tree import BTree, createMinimalBST, printTree


def get_children(node):
    children = []
    if node.left is not None:
        children.append(node.left)
    if node.right is not None:
        children.append(node.right)
    return children

def printPermutations(possibilities, data):
    if len(possibilities) == 0:
        print(data)
        return
    
    for i in range(len(possibilities)):
        node = possibilities[i]
        del possibilities[i]
        new_possibilities = get_children(node) + possibilities
        printPermutations(new_possibilities, data + " " + str(node.data))
        possibilities.insert(i,node)


def allSequences(root):
    results = []

    if root is None:
        return results

    prefix = []
    prefix.append(root.data)
    print(root.data)

    # recurse on left and right subtrees
    leftseq = allSequences(root.left)
    rightseq = allSequences(root.right)

    # weave together each list from the left and right sides
    print(prefix, leftseq, rightseq)
    for left in leftseq:
        for right in rightseq:
            weaved = weaveLists(left, right, prefix)
            for w in weaved:
                results.append(w)

    return results

def weaveLists(first, second, prefix):
    # one list is empty. add remainder to [a cloned] prefix and store result
    results = []
    if (len(first) == 0 or len(second) == 0):
        result = prefix
        [result.append(a) for a in first]
        [result.append(b) for b in first]
        results.append(result)
        return results
    
    # recurse with head of first added to the prefix.
    headFirst = first[0]
    newprefix = prefix
    newprefix.append(headFirst)
    newfirst = first[1:]
    results.append(weaveLists(newfirst, second, newprefix))
    
    # do the same thing with second, 
    headSecond = second[0]
    newprefix = prefix
    newprefix.append(headSecond)
    newsecond = second[1:]
    results.append(weaveLists(first, newsecond, newprefix))

    return results


if __name__=="__main__":
    array = [1, 2, 3, 4, 5]

    tree_root = createMinimalBST(array)
    printTree(tree_root)
    print(tree_root.data)
    results = allSequences(tree_root)
    print(results)

    printPermutations(get_children(tree_root), str(tree_root.data))
    