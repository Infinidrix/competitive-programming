# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def findBottom(self, root, depth = 0):
        if not(root.left or root.right):
            return root, depth
        resL = [0, depth - 1]
        resR = [0, depth - 1]
        if root.left:
            resL = self.findBottom(root.left, depth+1)
        if root.right:
            resR = self.findBottom(root.right, depth+1)
        if resL[1] >= resR[1]:
            return resL
        return resR
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.findBottom(root)[0].val
