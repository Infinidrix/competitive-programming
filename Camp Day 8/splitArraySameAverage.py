# https://leetcode.com/problems/split-array-with-same-average/

class Solution:
    
    def check_split(self, listed, sums, start, end, checked, other_sum, length, working_sum, working_length):
        temp = 10000000 if len(listed) <= 20 else 100
        
        if (working_length, (sums[end] - sums[start - 1] + working_sum) % temp, other_sum % temp) in checked or start > end:
            return False
        
        avg = (sums[end] - sums[start - 1] + working_sum)/(end - start + 1 + working_length)
        
        if avg == other_sum / length:
            return True
        
        checked.add((working_length, (sums[end] - sums[start - 1] + working_sum) % temp, other_sum % temp))
            
        return self.check_split(listed, sums, start, end - 1, checked, other_sum, length, working_sum + listed[end], working_length + 1) or self.check_split(listed, sums, start, end - 1, checked, other_sum + listed[end], length + 1, working_sum, working_length) or self.check_split(listed, sums, start + 1, end, checked, other_sum, length, working_sum  + listed[start], working_length + 1) or self.check_split(listed, sums, start + 1, end, checked, other_sum + listed[start], length + 1, working_sum, working_length)
        
    
    def splitArraySameAverage(self, A: List[int]) -> bool:
        sorted_a = sorted(A, reverse = True)
        
        if sorted_a[0] == sorted_a[-1]:
            return len(sorted_a) % 2 != 1
        
        sums = [sorted_a[0]] + [0 for i in range(len(A) - 1)]
        for i in range(1, len(sorted_a)):
            sums[i] = sums[i-1] + sorted_a[i]
            
        return self.check_split(sorted_a, sums, 1, len(A) - 2, set(), sorted_a[0] + sorted_a[-1], 2, 0, 0)
