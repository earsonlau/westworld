from sys import maxsize
def createstack():
    stack=[]
    return stack

def isemptystack(stack):
    return len(stack) == 0

def isfullstack(stack):
    return len(stack) == maxsize

def push(stack,e):
    if isfullstack(stack):
        stack.append(e)
        return 1
    return 0

def pop(stack):
    if isemptystack():
        return 0
    return stack.pop()

def peek(stack):
    if isemptystack(stack):
        return 0
    return stack[len(stack)-1]
