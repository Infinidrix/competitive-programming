# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = {}
        for i in range(len(position)):
            speed_map[position[i]] = speed[i]
        position.sort()
        arrival_time = [(target-position[i])/speed_map[position[i]] for i in range(len(position))]
        print(arrival_time)
        count = 1
        if arrival_time == []:
            return 0
        slowest = arrival_time[-1]
        for i in range(len(arrival_time), 0, -1):
            if arrival_time[i-1] > slowest:
                count += 1
                slowest = arrival_time[i-1]
        return count