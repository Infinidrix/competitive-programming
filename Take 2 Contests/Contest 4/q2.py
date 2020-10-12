# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        path = collections.deque()
        path.append((root, 0))
        prev = None
        level = -1
        
        while path:
            node = path.popleft()
            if node[0].val % 2 == node[1] % 2:
                return False
            
            if node[1] != level:
                level = node[1]
            elif prev == node[0].val or ((node[0].val - prev > 0 and node[1] % 2 == 1) or 
                                         (node[0].val - prev < 0 and node[1] % 2 == 0)):
                return False
            
            prev = node[0].val
            
            if node[0].left: path.append((node[0].left, level + 1))
            if node[0].right: path.append((node[0].right, level + 1))
        
        return True
                
            