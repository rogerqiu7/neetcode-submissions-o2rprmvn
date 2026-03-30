class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr,dc in directions:
                    new_row, new_col = row + dr,col + dc
                    if (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid[new_row][new_col] != 1):
                        continue
                    
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col))
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1

