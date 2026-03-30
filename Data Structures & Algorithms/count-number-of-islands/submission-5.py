class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0

        rows = len(grid)
        columns = len(grid[0])

        def dfs(row, column):

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for dr,dc in directions:
                new_row, new_col = row + dr, column + dc

                # if out of bounds or a 0, exit the recursion
                if (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= columns or grid[new_row][new_col] == "0"):
                    continue
                
                grid[new_row][new_col] = "0"

                # being recursion on its neighbor
                dfs(new_row,new_col)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":                    
                    grid[row][column] = "0"
                    islands += 1
                    dfs(row, column)
        
        return islands
