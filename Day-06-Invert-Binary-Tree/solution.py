# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    # I'll just swap the left and right children recursively.
    # Base case: empty tree
    if not root:
        return None
        
    # Swap the left and right pointers
    root.left, root.right = root.right, root.left
    
    # Recursively invert the subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root
