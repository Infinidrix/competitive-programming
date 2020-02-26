
# https://leetcode.com/problems/divisor-game/

class Solution:
    
    def run_game(self, n, visited):
        for i in range(1,n):
            if n % i == 0:
                if n - i not in visited:
                    self.run_game(n - i, visited)
                if not visited[n - i]:
                    visited[n] = True
                    return
        visited[n] = False
                
    
    def divisorGame(self, N: int) -> bool:
        result = {1:False}
        self.run_game(N, result)
        return result[N]
