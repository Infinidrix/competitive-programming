
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        all_sum = [0 for i in range(len(nums))]
        all_sum[0] = nums[0]
        all_sum[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            all_sum[i] = max(all_sum[i-2]+nums[i], all_sum[i-1])
        return all_sum[-1]
