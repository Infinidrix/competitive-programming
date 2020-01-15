# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        k_size_set = set()
        for i in range(len(nums)):
            if nums[i] in k_size_set:
                return True
            
            if len(k_size_set) == k:
                k_size_set.remove(nums[i-k])
            k_size_set.add(nums[i])
            
        return False
