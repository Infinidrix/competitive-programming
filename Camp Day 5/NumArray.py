
# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0 for i in range(len(nums) + 1)]
        self.sums[0] = 0
        for i in range(1, len(nums)+1):
            self.sums[i] = self.sums[i-1] + self.nums[i-1]
        
        #print(self.sums)
        
    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
