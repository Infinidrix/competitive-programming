# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class Solution:
    
    def preprocess(self, string):
        counter = 0
        result = []
        s = ""
        for i in string:
            if i == "-" and s == "":
                counter += 1
            elif i == "-" and s != "":
                result.append([int(s), counter])
                s = ""
                counter = 1
            else:
                s += i
        result.append([int(s), counter])
        return result
    
    def treeFromPreorder(self,root,preorder,index = 0):
        if index + 1 < len(preorder) and preorder[index + 1][1] - 1 == preorder[index][1]:
            root.left = TreeNode(preorder[index + 1][0])
            endIndex = self.treeFromPreorder(root.left,preorder,index + 1)
            if endIndex + 1 < len(preorder) and preorder[endIndex + 1][1] - 1 == preorder[index][1]:
                root.right = TreeNode(preorder[endIndex + 1][0]) 
                endIndex = self.treeFromPreorder(root.right,preorder,endIndex + 1)
            return endIndex
        return index
            
                
        
    def recoverFromPreorder(self, S: str) -> TreeNode:
        preorder = self.preprocess(S)
        print(preorder)
        root = TreeNode(preorder[0][0])
        self.treeFromPreorder(root,preorder)
        return root
            
