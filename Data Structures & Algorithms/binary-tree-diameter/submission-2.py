# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0

            left_d = dfs(node.left)
            right_d = dfs(node.right)
            dia = left_d + right_d

            self.res = max(self.res, dia)

            return max(left_d, right_d) + 1
        
        dfs(root)
        return self.res