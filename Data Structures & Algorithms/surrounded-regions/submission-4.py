class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row,col):
            board[row][col] = "T"
            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0<= new_row < rows and 0<= new_col<cols and board[new_row][new_col] == "O"):
                    board[new_row][new_col] = "T"
                    dfs(new_row,new_col)

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row,0)
            if board[row][cols-1] == "O":
                dfs(row,cols-1) 

        for col in range(cols):
            if board[0][col] == "O":
                dfs(0,col)
            if board[rows-1][col] == "O":
                dfs(rows-1,col) 

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"

        
