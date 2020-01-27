# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution:
    def see_right(self, root, depth, max_depth, view):
        if depth > max_depth:
            view.append(root.val)
            max_depth += 1
        if root.right:
            max_depth, view = self.see_right(root.right, depth + 1, max_depth, view)
        if root.left:
            max_depth, view = self.see_right(root.left, depth + 1, max_depth, view)
        return max_depth, view
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.see_right(root, 0, -1, [])[1]
