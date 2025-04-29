# store info in variable, think scratch paper for an equation
variable = "value"

# atomic variable types, ints, float, and strings
x = 5
y = 3.2
z = True

print("x has type",type(x))

x = [1,2,3]
y = x
z = [1,2,3]

print(x is y)
print(x is z)
print(x == z)

# collection variable types, strings, lists, tuples, dictionaries and sets

# Strings are sequences of characters
s = "Hello"

print(s[1]) # you can access pieces of the sequence

# Lists are ordered sequences of objects, any type combinations

L = [1,2,3,4,5,6]

# add to the list
L.append(100) 

# access items by index, starting at 0
print(L[1])

# Tuples are also ordered sequences of objects, but are immutable
t = (1,2,"here",99,100)

# accessed the same way
print(t[1])

# Dictionaries store key value pairs
d = {}

# assign a value
d[2] = "two"

# access the value
print(d[2])

# sets, collections of objects without duplicates
s = set()

s.add(1)
s.add(2)
s.add(1)

# Things to do with collections
a = "string"

# check the length
print(len(a))

# slice a piece of the collection
print(a[3:7])

# iterate over the collection
for char in a:
    print(char)

# Control Flow
# if
if 3 + 3 < 7:
    print("this will print")
else:
    print("this will never print")

# while loop continues while it is true
x = 1
while x<123:
    print(x, end=" ")
    x = x * 2

# try catch, catch and deal with errors
x = "not a number"
try:
    f = float(x)
except ValueError:
    print("You cant do that")

# functions can break up the control flow
def foo(x,y):
    # returns back to usual flow
    return x+y

# breaks usual flow to run function
print(foo(2,1))