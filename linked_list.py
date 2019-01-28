### Linked List implementation

import os


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __get_next__(self):
        if self.value is not None:
            return self.next
        else:
            return None # could be another value to represent that self.value is itself None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        thead = self.head
        while thead is not None:
            print (thead.value)
            thead = thead.next 

    def insertDataAtBeg(self, newdata):
        newnode = Node(value=newdata)
        newnode.next = self.head
        self.head = newnode 

    def insertDataBefore(self, newdata, beforedata):
        prev = self.head
        current = self.head 
        if current is None:
            newnode = Node(value=newdata)
            self.head = newnode
            return # or continue
        while (current.value != beforedata) or (current is not None):
            prev = current
            current = current.next
        if current is not None:
            newnode = Node(value=newdata)
            prev.next = newnode
            newnode.next = current 
        else:
            # the beforedata does not exist in the list
            # raise some error or do nothing
            print("{} does not exist in the list".format(beforedata))
    
    def deleteNode(self, nodeval):
        thead = self.head
        if thead is None:
            print("List is empty")
            return
        elif thead.value == nodeval:
            # the node to be removed is the head
            self.head = thead.next
            thead = None
            return
        else:
            prev = None
            while (thead is not None):
                if thead.value == nodeval:
                   break
                prev = thead
                thead = thead.next
            if thead == None:
                return

            prev.next = thead.next
            thead = None  

