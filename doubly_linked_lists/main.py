class ListNode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addfirst(self,item):
        self.addbetween(item, None, self.head)

    def addlast(self, item):
        self.addbetween(item, self.tail, None)
    
    def addbetween(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self.head:
            self.head = node
        if before is self.tail:
            self.tail = node
        self.length += 1

    def remove(self, node):
        before, after = node.prev, node.link
        if node is self.head:
            self.head = after
        else:
            before.link = after
        
        if node is self.tail:
            self.tail = before
        else:
            after.prev = before
        
        self.length -= 1
        return node.data
    
    def removefirst(self):
        return self.remove(self.head)
    
    def removelast(self):
        return self.remove(self.tail)
    
    def __len__(self):
        return self.length
    
    # add two list together
    def __iadd__(self, other):
        if other.head is not None:
            if self.head is None:
                self.head = other.head
            else:
                self.tail.link = other.head
                other.head.prev = self.tail
            self.tail = other.tail
            self.length = self.length + other.length

            other.__init__()
        return self