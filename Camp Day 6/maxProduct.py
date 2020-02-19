# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def postorder_traverse(self, root, listed):
        val = 0
        if root.left:
            self.postorder_traverse(root.left, listed)
            val += listed[-1]
        if root.right:
            self.postorder_traverse(root.right, listed)
            val += listed[-1]
            
        listed.append(val + root.val)
    
    def maxProduct(self, root: TreeNode) -> int:
        listed = []
        self.postorder_traverse(root, listed)
        max_product = 1
        for i in listed:
            max_product = max(max_product, (listed[-1] - i) * i)
        return max_product % (10 ** 9 + 7)
