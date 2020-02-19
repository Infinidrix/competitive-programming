# https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        queue = collections.deque()
        
        for i in range(len(seats)):
            if seats[i] == 1:
                queue.append(i)
                
        max_dist = 1
        while queue:
            curr = queue.popleft()
            for i in [-1, 1]:
                if 0 <= curr + i < len(seats) and seats[curr + i] == 0:
                    seats[curr + i] = seats[curr] + 1
                    max_dist = max(max_dist, seats[curr + i])
                    queue.append(curr+i)
        return max_dist - 1
                
