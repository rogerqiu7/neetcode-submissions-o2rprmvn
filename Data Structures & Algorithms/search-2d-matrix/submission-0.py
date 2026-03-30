class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sublist in matrix:
            for number in sublist:
                if number == target:
                    return True

        return False
