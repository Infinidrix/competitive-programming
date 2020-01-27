# https://leetcode.com/problems/minesweeper/

class Solution:
    def __init__(self):
        self.dir = [[-1, 0], [0, 1], [1, 0], [0, -1],
                    [-1, 1], [1, 1], [1, -1], [-1, -1]]
    
    def find_mines(self, board, x, y):
        count = 0
        for i in self.dir:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == "M":
                count += 1
        return count
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        check = click
        if board[check[0]][check[1]] == "M":
            board[check[0]][check[1]] = "X"
        elif board[check[0]][check[1]] == "E":
            mines = self.find_mines(board, check[0], check[1])
            if mines == 0:
                board[check[0]][check[1]] = "B"
                for i in self.dir:
                    new_x = check[0] + i[0]
                    new_y = check[1] + i[1]
                    if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == "E":
                        self.updateBoard(board, [new_x, new_y])
            else:
                board[check[0]][check[1]] = str(mines)
            
        return board
            
