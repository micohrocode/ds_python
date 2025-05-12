def bubblesort(l):
    for iteration in range(len(l)-1):
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                # the larger number always gets moved
                # to the end of the
                l[i], l[i+1] = l[i+1], l

# TODO: come back to learn about this one more
def selectionsort(l):
    n = len(l)

    # go through the whole list
    for i in range(n-1):
        max_index = 0
        # chekcing only the range that hasnt been sorted
        for index in range(n - i):
            if l[index] > l[max_index]:
                # the max index is moved up as the number
                # is greater
                max_index = index
        # place the number
        l[n-i-1], l[max_index] = l[max_index], l[n-i-1]

# TODO: read more about this
def insertionsort(l):
    n = len(l)

    # for each item in the list
    for i in range(n):
        # set j to the current un ordered
        # spot at the end of the list
        j = n - i - 1

        # check for a number that needs
        # moved
        while j<n-1 and l[j]>l[j+1]:
            # swap the numbers
            l[j], l[j+1] = l[j+1], l[j]
            # move j
            j+=1