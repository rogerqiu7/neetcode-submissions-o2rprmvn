class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            maxRight = i + 1
            while maxRight < n and heights[maxRight] >= height:
                maxRight += 1

            maxLeft = i
            while maxLeft >= 0 and heights[maxLeft] >= height:
                maxLeft -= 1

            maxRight -= 1
            maxLeft += 1

            maxArea = max(maxArea, height * (maxRight - maxLeft + 1))

        return maxArea