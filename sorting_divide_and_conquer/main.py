# mergesort:
# split into equal parts
# split until they cannot be split
# sort them now
# combine them
def merge(arr, l, m, r):
    n1 = m - 1 + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# quick sort
# choose a pivot
# all smaller to left of pivot
# larger to right of pivot
# do this again for the left and right side
# stops recursion when only one element left in subarray

def partition(array, low, high):
    # rightmost is pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low,high):
        # if its less than the pivot
        if array[j] <= pivot:
            # a swap is needed
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    
    # move pivot to its correct position
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i+1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi-1)
        quicksort(array, pi + 1, high)
