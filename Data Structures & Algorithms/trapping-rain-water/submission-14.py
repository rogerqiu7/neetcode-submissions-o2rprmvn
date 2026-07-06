class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        max_l = 0
        max_r = 0

        while l < r:
            if height[l] < height[r]:
                max_l = max(height[l], max_l)
                current = max_l - height[l]
                res += current
                l += 1
            else:
                max_r = max(height[r], max_r)
                current = max_r - height[r]
                res += current
                r -= 1
        return res