# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def printStack(stack):
            temp = []
            val = '->'
            for i in range(0,len(stack)):
                if(i is not len(stack)-1):
                    temp.append(str(stack[i]))
                else:
                    temp.append(str(stack[i]))
            s = val.join(temp)
            res.append(s)
        stack = []
        def inorderTraversal(root):
            if root is None:
                return
            else:
                stack.append(root.val)
                inorderTraversal(root.left)
                if(root.left is None and root.right is None):
                    printStack(stack)
                inorderTraversal(root.right)
                stack.pop()
    inorderTraversal(root)
        return res
