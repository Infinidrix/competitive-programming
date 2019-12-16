# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def return_sorted(self, root):
        values = []
        if root.left:
            values.extend(self.return_sorted(root.left))
        values.append(root.val)
        if root.right:
            values.extend(self.return_sorted(root.right))
        return values
    
    def bin_search(self, array, item, start = 0, end = None):
        if not end:
            end = len(array)
        mid = int (((start+end)/2 - 0.5) + 1)
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            return self.bin_search(array, item, mid, end)
        else:
            return self.bin_search(array, item, start, mid)
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        array = self.return_sorted(root)
        indexL = self.bin_search(array, L)
        indexR = self.bin_search(array, R)
        summ = 0
        for i in range(indexL, indexR+1):
            summ += array[i]
        return summ
