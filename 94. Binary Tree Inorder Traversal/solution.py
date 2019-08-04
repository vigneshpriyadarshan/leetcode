# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        collect = []
        if root is None:
            return collect
        else:
            current = root
            stack = []
            iterate = True
            while(iterate):
                if current is not None:
                    stack.append(current)
                    current = current.left
                else:
                    if(len(stack)>0):
                        current = stack.pop()
                        collect.append(current.val)
                        current = current.right
                    else:
                        iterate = False
            return collect
