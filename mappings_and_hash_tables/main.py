# mapping = an association between two things
# key value pairs

# basic setup
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return str(self.key) + ":" + str(self.value)
    
def mapput(l, key, value):
    for e in l:
        if e.key == key:
            e.value = value
            return
    l.append(Entry(key, value))

def mapget(l, key):
    for e in l:
        if e.key == key:
            return e.value
    raise KeyError

# TODO: perhaps come back and dive deeper here