"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Solution:
    
    def find_max_depth(self, root, depth):
        if not root:
            return depth
        if root.children:
            max_depth = depth
            for i in root.children:
                new_max = self.find_max_depth(i, depth + 1)
                if new_max > max_depth:
                    max_depth = new_max
            return max_depth
        return depth + 1
    
    def maxDepth(self, root: 'Node') -> int:
        return self.find_max_depth(root, 0)
