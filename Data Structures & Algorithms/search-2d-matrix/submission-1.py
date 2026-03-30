class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sublist in matrix:
            for i in sublist:
                if i == target:
                    return True
        return False