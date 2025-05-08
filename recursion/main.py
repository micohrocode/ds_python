# Recursion
# a function that calls itself
# have a base case to make sure it terminates at some point
# recursive calls should move towards the base case

def fib(k):
    # base case
    if k in [0,1]: return k
    # works towards the base case
    return fib(k-1) + fib(k-2)

# Euclids Algorithm
def gcd(a,b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(a,b % a)