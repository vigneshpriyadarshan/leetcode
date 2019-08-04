# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = []
        temp = []
        answer = []
        if root is None:
            return None
        queue.append(root)
        while(len(queue)>0):
            summ = 0
            inc = 0
            temp = []
            while(len(queue)>0):
                node = queue.pop(0)
                summ = summ + node.val
                inc = inc + 1
                if(node.left is not None):
                    temp.append(node.left)
                if(node.right is not None):
                    temp.append(node.right)

            answer.append(summ/inc)
            queue = temp.copy()
        return answer
