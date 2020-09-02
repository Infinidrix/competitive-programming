
# https://leetcode.com/problems/bulb-switcher-iii/

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        visited = [0 for i in range(50001)]
        start = 0
        count = 0
        max_index = 0
        for i in light:
            visited[i] = 1
            if i > max_index:
                max_index = i
                
            if start == i - 1:
                # print(f'This is start {start}')
                while start < len(visited) - 1 and visited[start + 1] == 1:
                    start += 1
                
                if max_index == start:
                    count += 1
                # print(f"this is start now {start}")
        return count
            
