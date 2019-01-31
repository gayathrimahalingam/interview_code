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
             
            
    