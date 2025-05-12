# TODO: find a video exaplanation of mergesort and quicksort
def mergesort(l):
    if len(l)<2:
        return
    
    # get the two halves of the list
    mid = len(l) // 2
    a = l[:mid]
    b = l[mid:]

    mergesort(a)
    mergesort(b)

    # combine them
    merge(a,b,l)

def merge(a,b,l):
    # index for a
    i = 0 
    # index for b
    j = 0

    while i < len(a) and j < len(b):
        # if the current a is smaller
        if a[i] < b[i]:
            # place the a number
            l[i+j] = a[i]
            # move the index
            i+=1
        else:
            # place the b number
            l[i+j] = b[j]
            # move the index
            j+=1

    # place all remaining numbers
    l[i+j:] = a[i:] + b[j:]

# iterators
class SimpleIterator:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <10:
            self.count += 1
            return self.count
        else:
            raise StopIteration

def quicksort(l, left = 0, right = None):
    if right is None:
        right = len(l)

    if right - left > 1:
        # divide it
        mid = partition(l, left, right)

        quicksort(l, left, mid)
        quicksort(l, mid+1, right)

def partition(l, left, right):
    pivot = right - 1
    # left index
    i = left
    # right index
    j = pivot - 1

    while i < j:
        # move i to point to something larger
        while l[i] < l[pivot]:
            i = i + 1

        # move j to point to something smaller
        while i < j and l[j] >= l[pivot]:
            j = j - 1

        # swap the elements if i < j
        if i<j:
            l[i], l[j] = l[j], l[i]
    
    if l[pivot] <= l[i]:
        l[pivot], l[i] = l[i], l[pivot]
        pivot = i

    return pivot