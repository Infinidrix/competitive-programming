# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/longest-univalue-path/

class Solution:
    def find_univalue(self, parent_val, root, is_root):
        self_path_l = self_path_r = maxi_l = maxi_r = 0
        if root.left:
            maxi_l, self_path_l = self.find_univalue(root.val, root.left, False)
        if root.right:
            maxi_r, self_path_r = self.find_univalue(root.val, root.right, False)
        max_path = max(self_path_l + self_path_r, maxi_l, maxi_r)
        
        if root.val == parent_val:
            return max_path, max(self_path_l, self_path_r) + 1
        else:
            return max_path, 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.find_univalue(None, root, True)[0]
        
