# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#https://leetcode.com/problems/maximum-binary-tree/

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            max_val = max(nums)
            max_index = nums.index(max_val)
            root = TreeNode(max_val)
            root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
            return root
        return None
