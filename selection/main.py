from sorting_divide_and_conquer import partition

def quickselect(l,k):
    return _quickselect(l,k,0,len(l))

def _quickselect(l,k,left,right):
    pivot = partition(l, left, right)
    if k <= pivot:
        return _quickselect(l, k, left, pivot)
    elif k == pivot + 1:
        return l[pivot]
    else:
        return _quickselect(l, k, pivot + 1, right)