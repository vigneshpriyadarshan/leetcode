# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    p_list = []
    q_list = []
    common_list = []

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            if(p.val == q.val):
                return Solution().isSameTree(p.left,q.left) and Solution().isSameTree(p.right,q.right)

            else:
                return False
        else:
            return False
