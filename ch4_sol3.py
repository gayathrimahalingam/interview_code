# Given a binary tree, design an algorithm which creates a linked list of all nodes at each depth

# solution: a modified pre-order traversal passing depth information 
# also a modified breadt first search works
# add root to linked list, then traverse each element in this linked list and create a new list


import os 
from linked_list import LinkedList
from binary_tree import BTree, createMinimalBST


def createLevelLinkedList(root):
    result = []
    current = LinkedList()
    if (root is not None):
        current.insertAtEnd(root)
    
    while (current.currentsize > 0):
        result.append(current)
        parents = current.head
        current = LinkedList()
        while (parents is not None):
            if (parents.value.left is not None):
                current.insertAtEnd(parents.value.left)
            if (parents.value.right is not None):
                current.insertAtEnd(parents.value.right)
            parents = parents.next
    return result

def printResult(result):
    for l in result:
        head = l.head
        while head is not None:
            print(head.value.data)
            head = head.next
        print ""


if __name__=="__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree_root = createMinimalBST(array)
    result = createLevelLinkedList(tree_root)
    
    printResult(result)

