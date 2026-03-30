class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for cell in row:
                if cell != "." and cell in seen:
                    return False 
                if cell != ".":
                    seen.add(cell)

        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]

                if cell != "." and cell in seen:
                    return False 
                if cell != ".":
                    seen.add(cell)

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):

                        cell = board[row][col]

                        if cell != "." and cell in seen:
                            return False 
                        if cell != ".":
                            seen.add(cell)

        return True