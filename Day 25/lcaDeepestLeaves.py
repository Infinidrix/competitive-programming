# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class Solution:
    
    def find_ancestor(self, root, depth):
        left_depth = right_depth = depth
        statL = statR = False
        Lnode = Rnode = None
        if root.left:
            statL, left_depth, Lnode = self.find_ancestor(root.left, depth + 1)
        if root.right:
            statR, right_depth, Rnode = self.find_ancestor(root.right, depth + 1)
        
        if right_depth < left_depth and statL:
            return True, left_depth, Lnode
        elif right_depth > left_depth and statR:
            return True, right_depth, Rnode
        elif left_depth == right_depth:
            return True, right_depth, root
        
        return False, max([left_depth, right_depth]), None
    
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.find_ancestor(root, 0)[2]
