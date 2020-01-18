# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class Solution:
    
    def add_even_grands(self, root, multiplier, sums):
        multiplier = multiplier[:]
        cur_multiplier = multiplier.pop(0)
        if root.val % 2 == 0:
            multiplier.append(1)
        else:
            multiplier.append(0)
        sums += root.val * cur_multiplier
        if root.right:
            sums = self.add_even_grands(root.right, multiplier, sums)
        if root.left:
            sums = self.add_even_grands(root.left, multiplier, sums)
        return sums
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.add_even_grands(root, [0, 0], 0)
