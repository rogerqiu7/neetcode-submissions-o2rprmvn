class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        islands = 0

        def dfs(row,col):
            grid[row][col] = "0"

            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0 <= new_row < rows and 0<= new_col < columns and grid[new_row][new_col] == "1"):
                    dfs(new_row,new_col)

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row,col)

        return islands
