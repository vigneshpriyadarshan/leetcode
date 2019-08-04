# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if (root is None or (root.left is None and root.right is None)):
            return root
        else:
            temp_left = root.left
            temp_right = root.right
            root.left = temp_right
            root.right = temp_left
            Solution().invertTree(root.left)
            Solution().invertTree(root.right)
            return root
