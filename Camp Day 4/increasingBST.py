# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/increasing-order-search-tree/

class Solution:
    
    def inorder_traversal(self, root):
        result = []
        if root:
            result.extend(self.inorder_traversal(root.left))
            result.append(root.val)
            result.extend(self.inorder_traversal(root.right))
        return result
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_array = self.inorder_traversal(root)
        #print(inorder_array)
        new_root = TreeNode(inorder_array[0])
        curr = new_root
        for i in range(1, len(inorder_array)):
            curr.right = TreeNode(inorder_array[i])
            curr = curr.right
        return new_root
