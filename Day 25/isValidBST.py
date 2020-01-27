# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def in_order_traversal(self, root):
        listed = []
        if root:
            listed.extend(self.in_order_traversal(root.left))
            listed.append(root.val)
            listed.extend(self.in_order_traversal(root.right))
        return listed
    
    def isValidBST(self, root: TreeNode) -> bool:
        inorder_array = self.in_order_traversal(root)
        for i in range(1, len(inorder_array)):
            if inorder_array[i-1] >= inorder_array[i]:
                return False
        return True
