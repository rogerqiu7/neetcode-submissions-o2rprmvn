class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        fresh = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        minutes = 0

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1

        while fresh > 0 and queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row+dr, col+dc
                    if (0<= new_row < rows and 0<=new_col<columns and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col))
                        fresh -= 1
            minutes += 1

        return minutes if not fresh else -1