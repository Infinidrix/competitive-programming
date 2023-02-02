class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(Counter(nums)) - (1 if 0 in nums else 0)