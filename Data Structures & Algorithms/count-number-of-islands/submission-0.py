class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row,column):
            queue = collections.deque()
            queue.append((row,column))
            visited.add((row,column))

            while queue:
                row, column = queue.popleft()
                directions = [[0,1], [1,0], [-1,0], [0,-1]]
                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc
                    if (new_row in range(rows) and
                        new_column in range(columns) and
                        grid[new_row][new_column] == "1" and
                        (new_row, new_column) not in visited):
                        queue.append((new_row, new_column))
                        visited.add((new_row, new_column)) 

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row,column)
                    islands += 1
        return islands