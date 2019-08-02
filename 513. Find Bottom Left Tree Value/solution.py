# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)
        done = False
        answer = None
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        while(len(queue)>0):
            arr = []
            while(len(queue)>0):
                node = queue.pop(0)
                if(node.left is not None):
                    arr.append(node.left)
                    print(node.left.val)
                if(node.right is not None):
                    arr.append(node.right)
                    print(node.right.val)
            if(len(arr)>0):
                answer = arr[0].val
            queue = arr
        return answer
