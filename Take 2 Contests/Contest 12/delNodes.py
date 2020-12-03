
# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse_and_delete(self, root, is_orphan, to_delete, output):
        if not root:
            return None
        
        is_deleted = root.val in to_delete
        root.left = self.traverse_and_delete(root.left, is_deleted, to_delete, output)
        root.right = self.traverse_and_delete(root.right, is_deleted, to_delete, output)
        
        if not is_deleted and is_orphan:
            output.append(root)
		
        return root if not is_deleted else None
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        output = []
        self.traverse_and_delete(root, True, to_delete, output)
        return output
