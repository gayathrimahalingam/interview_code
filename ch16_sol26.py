# calculate the value of an arithmetic expression

# assumption: The expression is given as an array of strings

import os 
from stack import Stack

# solution 1
# use two arrays "processing" and "result"

def calculate(expr):
    processing = []
    result = 0

    for i in range(0, len(expr)):
        current = expr[i]
        if i+1 < len(expr):
            next = expr[i+1]
        else:
            next = None
        processing = collapse(processing, current)

        if (next is None or next is "+" or next is "-"):
            result = applyOp(result, processing[0], processing[1])
            processing = []

    return result

def collapse(processing, current):
    if processing is None:
        return float(current)
    if current is None:
        val = processing[0]+processing[1]
        return float(val)
    value = applyOp(processing[1], current)

def applyOp(left, op, right):
    if (op == "+"):
        return left + right
    elif (op == "-"):
        return left - right
    elif (op == "*"):
        return left * right
    else:
        return right
# incomplete solution 1

# solution 2

def collapse(num1, num2, op):
    #print("Collapsing {} {} {}".format(num2, op, num1))
    return eval(str(num2) + op + str(num1))

def compute(expr):
    # have two stacks one for numbers and other for operators
    op_stack = Stack()
    num_stack = Stack()
    priority = {"+":1, "-":1, "*":2, "/":2, "%":2}

    for ex in expr:
        if ex.isdigit():
            num = float(ex)
            #print("Inserting {} in num_stack".format(num))
            num_stack.push(num)
        elif ex in priority.keys():
            if op_stack.is_empty() or (priority[ex] > priority[op_stack.peek()]):
                #print("Inserting {} in op_stack - high priority".format(ex))
                op_stack.push(ex)
            else:
                while (not op_stack.is_empty() and priority[ex] <= priority[op_stack.peek()]):
                    res = collapse(num_stack.remove(), num_stack.remove(), op_stack.remove())
                    num_stack.push(res)
                op_stack.push(ex)
        
    while not op_stack.is_empty():
        res = collapse(num_stack.remove(), num_stack.remove(), op_stack.remove())
        num_stack.push(res)
    return num_stack.remove()




if __name__ == "__main__":
    expression = ["2", "*", "3", "+", "5", "/", "6", "*", "3", "+", "15"]
    result = compute(expression)
    print(result)