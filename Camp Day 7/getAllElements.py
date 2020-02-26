
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def merge(self, list1, list2):
        list1.append(10**6)
        list2.append(10**6)
        result = []
        i = j = 0
        while i < len(list1) - 1 or j < len(list2) - 1:
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        return result
    
    def inorder_traverse(self, root, result):
        if root:
            self.inorder_traverse(root.left, result)
            result.append(root.val)
            self.inorder_traverse(root.right, result)
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        listed1 = []
        listed2 = []
        self.inorder_traverse(root1, listed1)
        self.inorder_traverse(root2, listed2)
        new_list = self.merge(listed1, listed2)
        return new_list
