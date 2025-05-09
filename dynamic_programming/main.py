# Dynamic programming
# solve problems by using the solutions to the same problem
# but on smaller instances

def dpMakeChange(coinValueList, change):
    # store the answer to the sub problems
    minCoins = [None]*(change+1)

    # compute number of coins needed
    for cents in range(change+1):
        # first assume all ones are used
        minCoins[cents] = cents

        # check if any coin leads to a better solution
        for c in coinValueList:
            if cents >= c:
                minCoins[cents] = min(minCoins[cents],minCoins[cents-c] + 1)

    return minCoins[change]

# Least common subsequence
def lcs(X,Y):
    t = {}
    for i in range(len(X)+1): t[(i,0)] = ""
    for j in range(len(Y)+1): t[(0,j)] = ""

    # for each letter in X
    for i, x in enumerate(X):
        # for each letter in Y
        for j, y in enumerate(Y):
            # if the two letters are the same
            if x==y:
                # add the matching letter
                t[(i+1,j+1)] = t[(i,j)] + x
            else:
                # if they dont match look at the options
                # the value from above
                # and the value from the left
                # keep the longest match youve seen so far
                t[(i+1,j+1)] = max([t[(i, j+1)], t[(i+1, j)]], key = len)
            print(t)

    # finallt return the bottom right with longest common subseqeunce
    return t[(len(X),len(Y))]