class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            big_stone = -heapq.heappop(stones)
            less_stone = -heapq.heappop(stones)
            if big_stone > less_stone:
                heapq.heappush(stones, -(big_stone - less_stone))
        return -heapq.heappop(stones) if len(stones) > 0 else 0