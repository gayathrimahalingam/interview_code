### Write code to remove duplicates from a linked list
### what if a buffer is not allowed

import os
from linked_list import LinkedList

def removeDups(llist):
    buffer = set()

    prev = None
    current = llist.head
    while (current != None):
        if current.value in buffer:
            # this is a duplicate
            prev.next = current.next
            current = None
            current = prev.next
        else:
            buffer.add(current.value)
            prev = current
            current = current.next 

def removeDupsWithoutBuffer(llist):
    current = llist.head
    while (current.next is not None):
        prev = current
        runner = current.next
        while (runner is not None):
            if runner.value == current.value:
                prev.next = runner.next 
            else:
                prev = runner 
            runner = runner.next
        current = current.next

if __name__ == "__main__":
    data = [2, 5, 10, 2, 8, 16, 22, 10, 8]
    linklist = LinkedList()
    for d in data:
        linklist.insertDataAtBeg(d)

    linklist.printList()
    #removeDups(linklist)
    removeDupsWithoutBuffer(linklist)
    linklist.printList()  

           
    