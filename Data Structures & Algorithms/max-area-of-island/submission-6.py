class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        columns = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row,col):
            area = 1
            grid[row][col] = 0

            for dr,dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0<=new_row<rows and 0<=new_col<columns and grid[new_row][new_col] == 1):
                    area += dfs(new_row,new_col)

            return area

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    current = dfs(row,col)
                    max_area = max(current, max_area)

        return max_area