### Stack implementation using lists

import os

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False
        
    def peek(self):
        # peek to look at top of the stack
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the stack")
        else:
            value = self.stack[-1]
            del self.stack[-1]
            return value

            # the other way is 
            # return self.stack.pop()