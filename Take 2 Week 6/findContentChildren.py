class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s = [-i for i in s]
        g = [-i for i in g]
        heapq.heapify(g)
        heapq.heapify(s)
        count = 0
        cookie = None
        while len(g) > 0 and (len(s) > 0 or cookie):
            child = -heapq.heappop(g)
            if not cookie: 
                cookie = -heapq.heappop(s)
            if child <= cookie:
                count += 1
                cookie = None
        return count