# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def traverse(count,root):
            if root.left is not None:
                node = root.left
                if node.left is None and node.right is None:
                    count = count + node.val
                
                else:
                    count = traverse(count,root.left)
        if((root.right is not None) or (root.left is None and root.right is not None)):
            return traverse(count, root.right)
        if root.left is None and root.right is None:
            return count
        return count
        if root is None:
            return 0
        else:
            count = 0
                count = traverse(count,root)
                return count
