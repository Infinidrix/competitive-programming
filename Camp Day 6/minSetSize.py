# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 0
            count[i] += 1
        new_count = sorted(count.values(), reverse = True)
        running_sum = 0
        for i in range(len(new_count)):
            running_sum += new_count[i]
            if running_sum >= len(arr)/2:
                return i+1
