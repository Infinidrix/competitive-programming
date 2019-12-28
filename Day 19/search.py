
# https://leetcode.com/problems/binary-search/submissions/

class Solution:
    def bin_search(self, nums, index_min, index_max, target):
        if index_min != index_max:
            index_mid = (index_min + index_max)//2
            if nums[index_mid] == target:
                return index_mid
            elif nums[index_mid] > target:
                return self.bin_search(nums, index_min, index_mid, target)
            else:
                return self.bin_search(nums, index_mid + 1, index_max, target)
        return -1
    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(nums, 0, len(nums), target)