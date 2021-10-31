"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1:
Partner 2:
Date:
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        return self.numElems == len(self.stack)

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        return self.numElems == 0

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        newSize = len(self.stack) * 2 if len(self.stack) != 0 else 1
        tmpStack = [None for x in range(0, newSize) ]
        tmpIndex = -1
        for elem in self.stack:
            tmpIndex += 1
            tmpStack[tmpIndex] = elem
        self.stack = tmpStack
        self.top = tmpIndex

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        if (self.isFull()):
            # import pdb; pdb.set_trace()
            self.resize()
            pass

        self.top += 1
        self.stack[self.top] = val
        self.numElems += 1
        pass
            

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        if (self.isEmpty() == True):
            return None
        ret = self.stack[self.top]
        self.top -= 1
        self.numElems -= 1
        return ret
