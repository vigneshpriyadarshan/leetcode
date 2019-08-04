# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        count = False
        def traverse(root: TreeNode, sum: int):
            count = False
            if root.left is None and root.right is None:
                sum = sum - root.val
                if(sum == 0 ):
                    return True
                else:
                    return False
            if root.left is None and root.right is not None:
                sum = sum - root.val
                return traverse(root.right,sum)
            if root.left is not None and root.right is None:
                sum = sum - root.val
                return traverse(root.left,sum)
            else:
                sum = sum - root.val
                count = traverse(root.left,sum)
                if(count):
                    return True
                else:
                    count = traverse(root.right,sum)
                    return count
        if root is None:
            return False
        else:
            count = traverse(root,sum)
        return count
