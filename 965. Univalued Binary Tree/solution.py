# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def searchDfs(root: TreeNode , val: int):
            if root is None:
                return True
            if (root.val != val):
                return False
            return searchDfs(root.left, val) and searchDfs(root.right, val)

        if root is None:
            return True
        else:
            return searchDfs(root,root.val)
