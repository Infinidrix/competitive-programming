class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for index in range(len(nums) - 1, -1, -1):
            count = len(nums) - index
            if count > nums[index]:
                if count - 1 > nums[index]:
                    return count - 1
                else: 
                    break
            elif index == 0 and count <= nums[0]:
                return count
        return -1 
                
                