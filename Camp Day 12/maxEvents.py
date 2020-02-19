# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        count = 0
        result = []
        heapq.heapify(result)
        location = 0
        for i in range(10**5 + 1):
            while location < len(events) and events[location][0] == i:
                heapq.heappush(result, events[location][1])
                location += 1
            while result and result[0] < i:
                heapq.heappop(result)
            if result:
                loc = heapq.heappop(result)
                # print(loc)
                count += 1
        return count
        
