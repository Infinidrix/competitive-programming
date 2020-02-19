# https://leetcode.com/problems/course-schedule-ii/

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for i in range(numCourses)]
        for i in prerequisites:
            courses[i[1]].append(i[0])
            
        dependencies = [0 for i in range(numCourses)]
        for i in courses:
            for j in i:
                dependencies[j] += 1
                
        queue = deque()
        for i in range(len(dependencies)):
            if dependencies[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for i in courses[curr]:
                dependencies[i] -= 1
                if dependencies[i] == 0:
                    queue.append(i)
        
        return result if len(result) == numCourses else []
