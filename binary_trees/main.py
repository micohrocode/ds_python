# binary tree - nodes at most have two children
# binary seach tree - all left nodes are less, all right are more
# in order traveral, all left nodes, root, then all right nodes
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def insert(root, key):
    # if there is no root, its just that node
    if root is None:
        return Node(key)
    if root.value == key:
        # the key already exists in the tree
        return root
    
    if root.value < key:
        # if the current root is less than the key
        # move to the right to place it
        root.right = insert(root.right, key)
    else:
        # else if the current root is greater than the key
        # move to the left to place it
        root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        # drill down to the left first
        inorder(root.left)
        print(root.value, end=" ")
        # then go to right after
        inorder(root.right)

r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)

# Print inorder traversal of the BST
inorder(r)