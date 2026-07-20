class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        queue = deque()
        fresh = 0
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1


        while queue and fresh > 0:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row+dr, col+dc
                    if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col]==1):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row,new_col))
            time += 1

        if fresh > 0:
            return -1
        else:
            return time