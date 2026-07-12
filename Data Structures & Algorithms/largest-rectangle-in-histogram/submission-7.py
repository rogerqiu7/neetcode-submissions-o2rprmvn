class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        for i in range(len(heights)):
            height = heights[i]
            l = i
            r = i

            while l >= 0 and heights[l] >= height:
                l -= 1
            while r < len(heights) and heights[r] >= height:
                r += 1

            current = (r - l - 1) * height

            res = max(res, current)

        return res