# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = Solution().maxDepth(root.left)
        right = Solution().maxDepth(root.right)
        max = 0
        if(left < right):
            max = right
        if(left > right):
            max = left
        if(left == right):
            max = left
        return max + 1
        
