# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return root
        trace_trail = [root]
        postOrder = []
        last_node = None
        while trace_trail:
            if last_node and last_node == trace_trail[-1].right:
                last_node = trace_trail.pop(-1)
                postOrder.append(last_node.val)
                continue
            if trace_trail[-1].left and last_node != trace_trail[-1].left:
                trace_trail.append(trace_trail[-1].left)
            elif trace_trail[-1].right:
                trace_trail.append(trace_trail[-1].right)
            else:
                last_node = trace_trail.pop(-1)
                postOrder.append(last_node.val)
        return postOrder
