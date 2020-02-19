# https://leetcode.com/problems/loud-and-rich/

class Solution:
    
    def fill_result(self, start, result, poorer, quiet):
        if result[start] != -1:
            return result[start]
        
        if len(poorer[start]) == 0:
            result[start] = start
            return result[start]
        
        answer = start
        min_quiet = quiet[start]
        
        for i in poorer[start]:
            temp = self.fill_result(i, result, poorer, quiet)
            
            if min_quiet > quiet[temp]:
                min_quiet = quiet[temp]
                answer = temp
    
        result[start] = answer
        return result[start]
    
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        poorer = [[] for i in range(len(quiet))]
        for i in richer:
            poorer[i[1]].append(i[0])
        result = [-1 for i in range(len(quiet))]
        # print(poorer)
        for i in range(len(result)):
            if result[i] == -1:
                self.fill_result(i, result, poorer, quiet)
                
        return result
