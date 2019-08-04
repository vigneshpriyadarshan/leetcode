# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        count = 1
        def traverse(count, root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return count + 1
            if root.left is None and root.right is not None:
                count = count + 1
                return traverse(count, root.right)
            if root.left is not None and root.right is None:
                count = count + 1
                return traverse(count, root.left)
            else:
                return min(traverse(count, root.left),traverse(count,root.right))+1
        if root is None:
            return 0
        if root .left is None and root.right is None:
            return 1
        if root.left is None and root.right is not None:
            return traverse(count, root.right)
        if root.left is not None and root.right is None:
            return traverse(count, root.left)
        else:
            left = traverse(count, root.left)
            right = traverse(count, root.right)
            if(left<right):
                return left
            else:
                return right

