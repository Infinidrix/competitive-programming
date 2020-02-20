
# https://leetcode.com/contest/weekly-contest-120/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dist_coins(self, root):
        new_balance = 0
        move_count = 0
        if root.left:
            balance, left_move_count = self.dist_coins(root.left)
            move_count += left_move_count
            root.val += balance
        if root.right:
            balance, right_move_count = self.dist_coins(root.right)
            move_count += right_move_count
            root.val += balance
        if root.val != 1:
            move_count += abs(root.val - 1)
            new_balance = root.val - 1
        return new_balance, move_count
    
    def distributeCoins(self, root: TreeNode) -> int:
        return self.dist_coins(root)[1]
