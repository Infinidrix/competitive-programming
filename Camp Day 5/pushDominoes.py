# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dirs = [0 for i in range(len(dominoes))]
        index = 0
        while index < len(dominoes):
            # print(index)
            if dominoes[index] == "R":
                count = 2
                dirs[index] = 1
                index += 1
                while index < len(dominoes) and dominoes[index] == ".":
                    dirs[index] = count
                    count += 1
                    index += 1
                
            elif dominoes[index] == "L":
                count = -1
                curr_index = index
                index += 1
                while curr_index >= 0 and (dirs[curr_index] == 0 or dirs[curr_index] >= abs(count)):
                    if dirs[curr_index] == abs(count):
                        if dirs[curr_index] != 1:
                            dirs[curr_index] = 0
                        break
                    else:
                        dirs[curr_index] = count
                        count -= 1
                        curr_index -= 1
            else:
                index += 1
        result = []
        for i in dirs:
            if i > 0:
                result.append("R")
            elif i == 0:
                result.append(".")
            else:
                result.append("L")
        return "".join(result)
                        
                
