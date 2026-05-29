class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            l = i - 1
            r = i +1

            while l >= 0 and heights[l] >= heights[i]:
                l -= 1

            while r < len(heights) and heights[r] >= heights[i]:
                r += 1

            current = (r - l - 1) * heights[i]

            max_area = max(current, max_area)

        return max_area