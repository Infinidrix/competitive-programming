# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val >= val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = (TreeNode(val))
        else:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = (TreeNode(val))
        return root
