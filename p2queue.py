"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Ian Liu (cl583)
Partner 2: Leo Han (nh185)
Date: 10/31/2021
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        ##### IMPLEMENT! ####
        return self.numElems == len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        return (self.numElems == 0)

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        newSize = (2 * len(self.queue)) if (len(self.queue) != 0) else 1
        tmpQueue = [None for i in range(0, newSize)]
        tmpIndex = 0
        for i in range(self.front, len(self.queue)):
            tmpQueue[tmpIndex] = self.queue[i]
            tmpIndex += 1
            pass

        for i in range(0, self.rear + 1):
            tmpQueue[tmpIndex] = self.queue[i]
            tmpIndex += 1
            pass

        self.front = 0
        self.rear = self.numElems - 1 if (len(self.queue) != 0) else 0
        self.queue = tmpQueue
                                          

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        if (self.isFull() == True):
            self.resize()
            pass
        
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = val
        self.numElems += 1

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        if (self.isEmpty() == True):
            return None
        
        ret = self.queue[self.front]
        self.front = (self.front + 1) % len(self.queue)
        self.numElems -= 1
        return ret
