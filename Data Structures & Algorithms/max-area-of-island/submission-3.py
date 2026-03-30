class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        largest = 0
        queue = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs():
            area = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 0
                        queue.append((new_row,new_col))
                        area += 1

            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row,col))
                    current = bfs()
                    if current > largest:
                        largest = current
        
        return largest