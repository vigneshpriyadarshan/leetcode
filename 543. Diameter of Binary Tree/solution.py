class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def lengthOfTree(root):
            if root is None:
                return 0
            else:
                left = lengthOfTree(root.left)
                right = lengthOfTree(root.right)
                return max(left,right)+1
        def diameter(root):
            if root is None:
                return 0
            else:
                lh = lengthOfTree(root.left)
                rh = lengthOfTree(root.right)
                ld = diameter(root.left)
                rd = diameter(root.right)
                return max(lh+rh,max(ld,rd))
        return diameter(root)
