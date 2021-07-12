# writing of binary search tree
# understaing and help in python code is taken from this website: https://qvault.io/python/binary-search-tree-in-python/
# All codes at least in this file belong to the website mentioned above.

#  BST is are basically binary tree with a specific property.
# The left subtree nodes are lesser than the root node. All the nodes of right subtree are more than root node.
# The subtrees of each nodes are also BST and have the same properties.

# Time and space complexities of binary search tree:
# given a tree ->> 3->2->1

# SEARCHING, INSERTING, DELETING:
        # worst case complexity: O(n) This means that we have traversed the whole tree in search of 1.
        # Average case: O(h) where h is the height of the tree. O(log n) is also true for avg cases which just the same thing.
        # Space complexity: O(n) for worst and average case.

# pros: Fast insertions, deletions, and searches O(logn) when the BST is balanced, and they are simple.
# Cons: they are slow for brute force, and if the tree is unbalanced the speed degrades to O(n). Also, because of the use of pointers to objects, BST take more memories than arrays, but it also depends on the implementation.


class BSTNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

# insert function
def insert(self, value):
    if not self.value:
        self.value = value
        return

    if self.value == value:
        return

    if value < self.value:
        if self.left:
            self.left.insert(value)
            return
        self.left = BSTNode(value)
        return

    if value < self.value:
        if self.right:
            self.right.insert(value)
            return
        self.right = BSTNode(value)


# min and max functions
def get_min(self):
    current = self
    while current.left is not None:
        current = current.left              # because left side will have the min value
    return current.value

def get_max(self):
    current = self
    while current.right is not None:
        current = current.right
    return current.value

# exists method to check the given value exists or not
def exists(self, value):
    if value = self.value:
        return True

    if value < self.value:
        if self.left == None:
            return False
        return self.left.exists(value)

    if self.right == None:
        return False
    return self.right.exists(value)

# inorder--left, current, right
def inorder(self, values):
    if self.left is not None:
        self.left.inorder(values)
    if self.value is not None:
        values.append(self.value)
    if self.right is not None:
        self.right.inorder(values)
    return values

# preorder-- current, left, right
def preorder(self, values):
    if self.value is not None:
        values.append(self.value)
    if self.left is not None:
        self.left.preorder(values)
    if self.right is not None:
        self.right.preorder(values)
    return values

# postorder-- left, right, current
def postorder(self, values):
    if self.left is not None:
        self.left.postorder(values)
    if self.right is not None:
        self.right.postorder(values)
    if self.value is not None:
        values.append(self.value)
    return values

    