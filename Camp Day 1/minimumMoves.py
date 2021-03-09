class Solution:
    
    def minimumMoves(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        # head, tail, moves
        queue.append(((0, 1), (0, 0), 0))
        visited = {((0, 1), (0, 0)),}
        
        # head move, tail move
        neighbours = (
            ((0,1), (0, 1)), # move right
            ((1, 0), (1, 0)), # move down
            ((1, -1), (0, 0)), # rotate clockwise
            ((-1, 1), (0, 0)) # rotate counterclockwise
        )
        while queue:
            head, tail, moves = queue.popleft()
            max_pos = len(grid) - 1
            if head == (max_pos, max_pos) and tail == (max_pos, max_pos - 1):
                return moves
            
            for index, neighbour in enumerate(neighbours):
                head_move, tail_move = neighbour
                new_head = (head[0] + head_move[0], head[1] + head_move[1])
                new_tail = (tail[0] + tail_move[0], tail[1] + tail_move[1])
                
                if (self.is_valid(grid, new_head, new_tail, visited) and 
                    self.check_rotate(index, grid, head, tail)):
                    
                    visited.add((new_head, new_tail))
                    queue.append((new_head, new_tail, moves + 1))
        return -1
    
    def check_rotate(self, index, grid, head, tail):
        if index < 2:
            return True
        elif index == 2:
            return head[0] == tail[0] and grid[head[0] + 1][head[1]] == 0
        else: 
            return head[1] == tail[1] and grid[head[0]][head[1] + 1] == 0
    
    def is_valid(self, grid, new_head, new_tail, visited):
        return (0 <= new_head[0] < len(grid) and 
                0 <= new_head[1] < len(grid) and 
                0 <= new_tail[0] < len(grid) and 
                0 <= new_tail[1] < len(grid) and # check boundaries
                grid[new_head[0]][new_head[1]] == 0 and 
                grid[new_tail[0]][new_tail[1]] == 0 and # check if can be placed 
                (new_head, new_tail) not in visited) # check if visited
            
            
