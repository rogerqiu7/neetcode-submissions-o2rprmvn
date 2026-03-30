class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest_island = 0

        rows = len(grid)
        columns = len(grid[0])

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(row,col):

            if (row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] == 0):
                return 0
                
            grid[row][col] = 0
            area = 1
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                area += dfs(new_row, new_col)

            return area
                
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    island_area = dfs(row,column)
                    if island_area > largest_island:
                        largest_island = island_area
        
        return largest_island

