# https://leetcode.com/problems/minimum-distance-between-bst-nodes/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder_sort(self, root):
        inorder_array = []
        if root:
            inorder_array.extend(self.inorder_sort(root.left))
            inorder_array.append(root.val)
            inorder_array.extend(self.inorder_sort(root.right))
        return inorder_array
            
    
    def minDiffInBST(self, root: TreeNode) -> int:
        sorted_list = self.inorder_sort(root)
        mini = sorted_list[1] - sorted_list[0]
        for i in range(1, len(sorted_list)):
            if sorted_list[i] - sorted_list[i-1] < mini:
                mini = sorted_list[i] - sorted_list[i-1]
        return mini
