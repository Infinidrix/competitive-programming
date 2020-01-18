# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/path-sum/

class Solution:
    
    def has_path_sum(self, root, req_sum, cur_sum, depth):
        if not root:
            return None
        
        elif not (root.left or root.right):
            if cur_sum == None:
                cur_sum = 0
            return cur_sum + root.val
        
        else:
            if cur_sum == None:
                cur_sum = 0
            children = [root.left, root.right]
            for i in children:
                new_sum = self.has_path_sum(i, req_sum, cur_sum + root.val, depth + 1)
                if new_sum == req_sum:
                    return new_sum
        
        
                
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if sum == self.has_path_sum(root, sum, None, 0):
            return True
        return False
