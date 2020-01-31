class Solution:
    
    def add_all(self, nums, target, curr, running_sum, max_sum, tracker):
        if curr == len(nums) or (target < running_sum - max_sum[curr] or target > running_sum + max_sum[curr]):
            return int(running_sum == target)
        if curr in tracker and running_sum in tracker[curr]:
            return tracker[curr][running_sum]
        count = 0
        count += self.add_all(nums, target, curr+1, running_sum + nums[curr], max_sum, tracker)
        count += self.add_all(nums, target, curr+1, running_sum - nums[curr], max_sum, tracker)
        if curr not in tracker:
            tracker[curr] = {}
        tracker[curr][running_sum] = count
        return count
    
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        max_sum = [0 for i in range(len(nums))]
        running_sum = 0
        for i in range(len(nums), 0, -1):
            running_sum += nums[i-1]
            max_sum[i-1] = running_sum
        tracker = {}
        return self.add_all(nums, S, 0, 0, max_sum, tracker)
