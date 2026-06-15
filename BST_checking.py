class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        def validate(node, low, high):
            # An empty node is a valid BST
            if not node:
                return True
            
            # Current node value must be strictly between low and high bounds
            if not (low < node.data < high):
                return False
            
            # Left child must be < node.data; Right child must be > node.data
            return validate(node.left, low, node.data) and validate(node.right, node.data, high)
            
        return 1 if validate(root, float('-inf'), float('inf')) else 0
