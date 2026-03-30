class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
    
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def bfs(start_row, start_col):
            """BFS helper to explore entire island"""
            queue = deque([(start_row, start_col)])
            grid[start_row][start_col] = '0'  # Mark as visited
            
            # 4 directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    # Check bounds and if it's unvisited land
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols and 
                        grid[new_row][new_col] == '1'):
                        
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = '0'  # Mark as visited
        
        # Main loop: scan entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1      # Found new island
                    bfs(r, c)         # Explore entire island
        
        return islands