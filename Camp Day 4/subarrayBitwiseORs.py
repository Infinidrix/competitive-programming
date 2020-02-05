
# https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result = set()
        temp1 = set()
        max_size = 0
        for i in A:
            temp2 = set()
            temp2.add(i)
            for j in temp1:
                temp2.add(i | j)     
            for j in temp2:
                result.add(j)
            max_size = max(max_size, len(temp2))
            temp1 = temp2
        print(max_size)
        return len(result)
