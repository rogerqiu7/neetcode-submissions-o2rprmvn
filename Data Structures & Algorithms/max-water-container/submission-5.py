class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)

                max_amount = max(area, max_amount)

        return max_amount