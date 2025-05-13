# tree, hierarchical structure
# nodes
# nodes have 0 or more children
# nods have at most one parent
# root - first node of the tree, no parent
# leaf nodes - no children
# path - sequence of nodes in which
# each node is a child of a previous node
# depth - from that node to root
# height - max depth of any node in the tree
class Tree:
    def __init__(self, l):
        iterator = iter(l)
        self.data = next(iterator)
        # children generated as trees
        self.children = [Tree(c) for c in iterator]

    def _listwithlevels(self, level, trees):
        # add the node
        trees.append(" "*level+str(self.data))
        for child in self.children:
            # add each of its children
            # moving the levels up
            child._listwithlevels(level + 1, trees)

    def __str__(self, level=0):
        trees = []
        self._listwithlevels(0, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            # for each child return the max height
            return 1 + max(child.height() for child in self.children)

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)
    
    # preorder traversal - parent first then children
    def printpreorder(self):
        print(self.data)
        for child in self.children:
            printpreorder(child)

    # postorder traversal - children and then parent
    def printpostorder(self):
        for child in self.children:
            printpostorder(child)
        print(self.data)