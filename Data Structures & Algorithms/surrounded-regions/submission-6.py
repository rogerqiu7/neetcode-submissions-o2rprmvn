class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col):
            if board[row][col] != "O":
                return

            board[row][col] = "T"

            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col] =="O"):
                    dfs(new_row, new_col)

        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)

        for i in range(cols):
            dfs(0,i)
            dfs(rows-1,i)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
        

            

