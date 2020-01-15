# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/most-frequent-subtree-sum/

class Solution:
    def addNodes(self, root):
        if root:
            Rsummation, Rfreq_sum = self.addNodes(root.right)
            Lsummation, Lfreq_sum = self.addNodes(root.left)
            for i in Lfreq_sum.keys():
                if i in Rfreq_sum:
                    Rfreq_sum[i] += Lfreq_sum[i]
                else:
                    Rfreq_sum[i] = Lfreq_sum[i]               
                
            new_sum = Lsummation + Rsummation + root.val
            if new_sum in Rfreq_sum:
                Rfreq_sum[new_sum] += 1
            else:
                Rfreq_sum[new_sum] = 1
            return new_sum, Rfreq_sum
        else:
            return 0, {}
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        summer, freq_dict = self.addNodes(root)
        maxi = 0
        nums = []
        for i in freq_dict.keys():
            if maxi < freq_dict[i]:
                nums = [i]
                maxi = freq_dict[i]
            elif maxi == freq_dict[i]:
                nums.append(i)
        return nums
