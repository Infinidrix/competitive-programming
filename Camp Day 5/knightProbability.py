# https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    
    def make_neigh(self, size):
        dirs = [[-1, -2], [1, 2], [1, -2], [-1, 2],
                [-2, -1], [2, 1], [2, -1], [-2, 1]]
        result = [[[] for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                for k in dirs:
                    if (0 <= i + k[0] < size and 
                        0 <= j + k[1] < size):
                        result[i][j].append((i+k[0], j + k[1]))
        return result
    
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        neighbours = self.make_neigh(N)
        moves = [{} for i in range(K)]
        if K == 0:
            if 0 <= r < N and 0 <= c < N:
                return 1
            else:
                return 0
        moves[0][(r, c)] = 1
        for i in range(1, K):
            for j in moves[i-1]:
                for k in neighbours[j[0]][j[1]]:
                    if k not in moves[i]:
                        moves[i][k] = 0
                    moves[i][k] += moves[i-1][j]
        # print(moves)
        result = 1
        for i in moves:
            sums = 0
            count = 0
            for j in i:
                sums += i[j] * len(neighbours[j[0]][j[1]])/8
                count += i[j]
            if count == 0:
                return 0
            result *= sums/count
        return result
