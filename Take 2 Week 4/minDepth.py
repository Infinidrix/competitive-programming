# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        path = collections.deque()
        path.append((root, 1))
        
        while path:
            node = path.popleft()
            
            if not (node[0].left or node[0].right):
                return node[1]
            
            if node[0].left: path.append((node[0].left, node[1] + 1))
            if node[0].right: path.append((node[0].right, node[1] + 1))
        return "WHATTT!!! YOu shouldn't have come here"
        