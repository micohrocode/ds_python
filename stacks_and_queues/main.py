# Stack
# push = add a new item to the stack
# pop = remove and return the next item (LIFO)
# peek = return the next item in LIFO ordering
# size = return the number of items in the stack
# is empty = True if no items in the stack

class ListStack:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.append(item)

    def pop(self):
        try:
            return self.list.pop()
        except IndexError:
            # handle errors to better 
            # describe the class
            raise RuntimeError("pop from empty stack")

    def peek(self):
        return self.list[-1]

    def __len__(self):
        return len(self.list)

    def isempty(self):
        return len(self.list) == 0
    
# Queue
# enqueue = add a new item to the queue
# dequeue = remove and return the next item FIFO
# peek = return without removing the next item FIFO
#  __len__ = return number of items in the queue
# isempty = return True is the queue has no items

class ListQueueSimple:
    def __init__(self):
        self.list = []
    
    def enqueue(self,item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def __len__(self):
        return len(self.list)

    def isempty(self):
        return len(self.list) == 0

