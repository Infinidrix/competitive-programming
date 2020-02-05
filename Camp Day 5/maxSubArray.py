
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        curr_max = nums[0]
        end = 0
        while end < len(nums):
            running_sum += nums[end]
            if running_sum > curr_max:
                curr_max = running_sum
            if running_sum < 0:
                running_sum = 0
            end += 1
        return curr_max
