# https://leetcode.com/problems/course-schedule/

class Solution:
    
    def dfs(self, courses, start, visited):
        visited.add(start)
        for i in courses[start]:
            if i in visited:
                return True
            if self.dfs(courses, i, visited):
                return True
        visited.remove(start)
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        for i in prerequisites:
            courses[i[0]].append(i[1])
        visited = set()
        for i in range(len(courses)):
            if i not in visited and self.dfs(courses, i, set()):
                return False
            visited.add(i)
        return True
