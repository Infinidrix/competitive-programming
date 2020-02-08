
# https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    
    def longest_chain(self, pairs, max_length, i):
        result = 1
        curr = pairs[i]
        for j in range(len(pairs)):
            if pairs[j][1] < curr[0]:
                if j not in max_length:
                    self.longest_chain(pairs, max_length, j)
                result = max(result, max_length[j] + 1)
        max_length[i] = result
        return result
                        
    
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        max_length = {}
        result = 0
        for i in range(len(pairs)):
            result = max(result, self.longest_chain(pairs, max_length, i))
        # print(max_length)
        return result
