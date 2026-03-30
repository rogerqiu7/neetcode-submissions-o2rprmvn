class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        queue = deque()

        def bfs():
            while queue:
                row, column = queue.popleft()
                directions = [[1,0], [0,1], [-1,0], [0,-1]]
                for dr, dc in directions:
                    new_row, new_col = row + dr, column + dc
                    if (0 <= new_row < rows and 0 <= new_col < columns and grid[new_row][new_col] == "1"):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = "0"

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    queue.append((row,column))
                    bfs()

        return islands