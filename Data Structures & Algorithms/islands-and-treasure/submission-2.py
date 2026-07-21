class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==2147483647):
                    grid[new_row][new_col] = grid[row][col] + 1
                    queue.append((new_row, new_col))
