class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(grid,row,col,ocean):
            if (row, col) in ocean:
                return

            ocean.add((row,col))

            for dr,dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] >= grid[row][col]):
                    dfs(grid,new_row,new_col, ocean)
            
        for i in range(rows):
            dfs(heights,i,0,pacific)
            dfs(heights,i,cols-1,atlantic)

        for i in range(cols):
            dfs(heights,0,i,pacific)
            dfs(heights,rows-1,i,atlantic)

        res = []

        for ele in pacific:
            if ele in atlantic:
                res.append(ele)

        return res

