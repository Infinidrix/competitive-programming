# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if not t1:
            t1 = TreeNode(0)
            if not t2:
                return None

        if not t2:
            t2 = TreeNode(0)
        root = TreeNode(t1.val + t2.val)

        if t1.left or t2.left:
            root.left = self.mergeTrees(t1.left, t2.left)
        if t1.right or t2.right:
            root.right = self.mergeTrees(t1.right, t2.right)
        
        return root
        
