# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        queue = []
        store = []
        if root is None:
            return None
        queue.append(root)
        while(len(queue)>0):
            node = queue.pop(0)
            store.append(node.val)
            if(node.left is not None):
                queue.append(node.left)
            if(node.right is not None):
                queue.append(node.right)
        result = 0
        answer = store.copy()
        if(len(answer)==1):
            return False
        for i in range(0,len(answer)):
            target = k - answer[i]
            answer1 = []
            answer2 = []
            if(i>0 or i == len(answer)-1):
                answer1 = answer[0:i-1]
            if(i<len(answer)-1 or i == 0):
                answer2 = answer[i+1:len(answer)]
            if((target in answer1) or (target in answer2)):
                result = 1
                break
            else:
                continue
        if(result == 1):
            return True
        else:
            return False


        
