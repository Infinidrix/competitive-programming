# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_from = [1 for i in range(len(nums))]
        for i in range(len(length_from) - 1, -1, -1):
            length = 0
            for j in range(i, len(length_from)):
                # print("got here", i, j, nums[j], nums[i])
                if nums[j] > nums[i]:
                    length = max(length, length_from[j])
            length_from[i] += length
        return max(length_from) if length_from else 0
