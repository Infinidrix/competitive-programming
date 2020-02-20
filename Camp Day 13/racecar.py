
# https://leetcode.com/problems/race-car/

class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque()
        moves = {}
        moves[(0, 0, 1)] = 0
        queue.append((0, 0, 1))
        while queue:
            curr = queue.popleft()
            new_move = curr[0] + curr[2] * (2 ** curr[1])
            if new_move == target:
                return moves[curr] + 1
            new_state = (new_move, curr[1] + 1, curr[2])
            if new_state not in moves:
                
                moves[new_state] = moves[curr] + 1
                queue.append(new_state)
            new_state = (curr[0], 0, -curr[2])
            if new_state not in moves:
                
                moves[new_state] = moves[curr] + 1
                queue.append(new_state)
