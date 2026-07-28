# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, largestval = stack.pop()
            if largestval <= node.val:
                res += 1
                
            largestval = max(largestval, node.val)


            if node.right: stack.append((node.right, largestval))
            if node.left: stack.append((node.left, largestval))

        return res


        