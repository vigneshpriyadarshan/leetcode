# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        stackleft = []
        stackright = []
        result1 = []
        result2 = []
        def traverse(root,stack):
            if root is None:
                return
            if root.left is None and root.right is None:
                return root.val
            else:
                stack.append(traverse(root.left,stack))
                stack.append(traverse(root.right,stack))
                return stack
        if root1 is None and root2 is not None:
            traverse(root2,stackright)
        if root2 is None and root1 is not None:
            traverse(root1,stackleft)
        if root1.left is None and root1.right is None and root2.left is None and root2.right is None:
            stackleft.append(root1.val)
            stackright.append(root2.val)
        if root1 is not None and root2 is not None:
            traverse(root1,stackleft)
            traverse(root2,stackright)
        result1.append([x for x in stackleft if type(x) == type(1)])
        result2.append([x for x in stackright if type(x) == type(1)])
        if(result1 == result2):
            return True
        else:
        return False
