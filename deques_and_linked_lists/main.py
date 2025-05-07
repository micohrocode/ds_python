# deque
# doubly ended queue, acts like a stack and a queue
class ListDeque:
    def __init__(self):
        self.list = []

    def addfirst(self,item):
        self.list.insert(0,item)

    def addlast(self,item):
        self.list.append(item)

    def removefirst(self):
        return self.list.pop(0)
    
    def removelast(self):
        return self.list.pop()
    
    def __len__(self):
        return len(self.list)
    


# Linked Lists
# allows us to insert at the beginning quickly
class ListNode:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def addfirst(self, item):
        self.head = ListNode(item, self.head)
        if self.tail is None:
            self.tail = self.head
        self.length += 1
    
    def addlast(self, item):
        if self.head is None:
            self.addfirst(item)
        else:
            self.tail.link = ListNode(item)
            self.tail = self.tail.link
            self.length += 1

    def removefirst(self):
        item = self.head.data
        self.head = self.head.link
        if self.head is None: 
            self.tail = None
        self.length -= 1
        return item
    
    def removelast(self):
        if self.head is self.tail:
            return self.removefirst()
        else:
            currentNode = self.head
            while currentNode.link is not self.tail:
                currentNode = currentNode.link
            item = self.tail.data
            self.tail = currentNode
            self.tail.link = None
            self.length -=1
            return item
    
    def __len__(self):
        return self.length
        
class LinkedQueue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self,item):
        self.list.addlast(item)

    def dequeue(self):
        return self.list.removefirst()
    
    def peek(self):
        item = self.list.removefirst()
        self.list.addfirst(item)
        return item
    
    def __len__(self):
        return len(self.list)
    
    def isempty(self):
        return len(self) == 0
    
