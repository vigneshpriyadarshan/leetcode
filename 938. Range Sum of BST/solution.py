# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is not None:
            stack = []
            current = root
            iterate = True
            sum = 0
            while(iterate):
                if current is not None:
                    stack.append(current)
                    current = current.left
                elif(len(stack)>0):
                    current = stack.pop()
                    if(current.val >= L and current.val <= R):
                        sum = sum + current.val
                    current = current.right
                else:
                    iterate = False
            return sum
