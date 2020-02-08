
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    
    def roll_dice(self, rolls, faces, target, checked):
        if target <= 0:
            return 0
        if rolls == 1:
            return 1 if target <= faces else 0
        if (rolls, target) in checked:
            return checked[(rolls, target)]
        max_count = 0
        for i in range(1, faces + 1):
            max_count += self.roll_dice(rolls - 1, faces, target - i, checked)
        checked[(rolls, target)] = max_count
        return max_count
            
            
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.roll_dice(d, f, target,{})%(10**9 + 7)
