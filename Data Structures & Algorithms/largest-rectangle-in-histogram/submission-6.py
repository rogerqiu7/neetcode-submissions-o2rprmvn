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
            current = height * (r-l-1)
            res = max(current, res)

        return res

