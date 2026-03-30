class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col):
            if (0 > row or row >= rows or 0 > col or col >= cols or board[row][col] != "O"):
                return
            
            board[row][col] = "T"

            for dr,dc in directions:
                new_row, new_col = row + dr, col + dc
                dfs(new_row, new_col)
        
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row,0)
            if board[row][cols-1] == "O":
                dfs(row, cols-1)

        for col in range(cols):
            if board[0][col] == "O":
                dfs(0,col)
            if board[rows-1][col] == "O":
                dfs(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"

        
