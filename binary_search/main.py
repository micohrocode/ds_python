def bs(l, item):
    left, right = 0, len(l)

    while right - left > 1:
        # find the middle
        median = (right+left) // 2
        if item < l[median]:
            # if its lower than the middle
            # check the left
            right = median
        else:
            # else check the right
            left = median

    return right > left and l[left] == item

