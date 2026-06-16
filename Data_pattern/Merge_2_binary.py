class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    # If one node is empty, return the other
    if not root1:
        return root2
    if not root2:
        return root1
    
    # Sum overlapping values
    merged = TreeNode(root1.val + root2.val)
    
    # Recursively merge left and right subtrees
    merged.left = mergeTrees(root1.left, root2.left)
    merged.right = mergeTrees(root1.right, root2.right)
    
    return merged
