# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/all-possible-full-binary-trees/

class Solution:
    
    def merge(self, root_val, left, right):
        result = []
        for i in left:
            for j in right:
                root = TreeNode(root_val)
                root.left = i
                root.right = j
                result.append(root)
        return result
    
    def all_possible(self, listed):
        if len(listed) == 1:
            return [TreeNode(listed[0])]
        if not listed:
            return [None]
        result = []
        for i in range(2, len(listed), 2):
            left_children = self.all_possible(listed[1:i])
            right_children = self.all_possible(listed[i:])
            result.extend(self.merge(listed[0], left_children, right_children))
        return result
    
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        listed = [0 for i in range(N)]
        return self.all_possible(listed)
