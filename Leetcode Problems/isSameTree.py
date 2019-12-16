# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        t1, t2 = p, q
        if not t1 or not t2:
            if not t2 and not t1:
                return True
            return False
        exist_left = t1.left or t2.left
        exist_right = t1.right or t2.right
        all_left = t1.left and t2.left
        all_right = t1.right and t2.right
        correct = (exist_left and all_left) or ((not exist_left) and (not all_left))
        correct = correct and ((exist_right and all_right) or ((not exist_right) and (not all_right)))
        if all_right:
            correct = correct and self.isSameTree(t1.right, t2.right)
        if all_left:
            correct = correct and self.isSameTree(t1.left, t2.left)
            
        return correct and (t1.val == t2.val)
