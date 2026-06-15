class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def check(self, root) -> int:
        self.leaf_level = -1
        
        def dfs(node, level):
            if not node:
                return True
            
            # Check if it is a leaf node
            if not node.left and not node.right:
                if self.leaf_level == -1:
                    self.leaf_level = level
                    return True
                return level == self.leaf_level
            
            # Recurse for left and right subtrees
            return dfs(node.left, level + 1) and dfs(node.right, level + 1)
            
        return 1 if dfs(root, 0) else 0
