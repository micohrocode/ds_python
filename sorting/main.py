def bubblesort(l):
    for iteration in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                # the larger number always gets moved
                # to the end of the
                l[i], l[i+1] = l[i+1], l

# selection sort:
# find the smallest element and swap it with the current index
def selectionsort(l):
    for ind in range(len(l)):
        min_index = ind

        for j in range(ind+1,size):
            # select the min element
            if l[j] < l[min_index]:
                min_index = j

        # swap the elements
        l[ind], l[min_index] = l[min_index], l[ind]

# insertion sort
# essentially work backwards, check for numbers greater than
# the one you are check and move them forward
# place the element you are checking where it should go
def insertionsort(l):
    n = len(l)

    if n<= 1:
        return
    
    # start from the second element
    for i in range(1,n):
        # element to check
        key = l[i]

        j = i - 1
        while j>=0 and key<l[j]:
            # move elements to the right
            l[j+1] = l[j]
            j -= 1
        
        # insert the key element to where it should be
        l[j+1] = key