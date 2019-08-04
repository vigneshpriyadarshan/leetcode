# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return NULL
        search = root
        while search is not None:
            if search.val == val:
                return search
            elif(val < search.val):
                search = search.left
            else:
                search = search.right
