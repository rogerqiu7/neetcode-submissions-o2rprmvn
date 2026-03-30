class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[l]
        r_max = height[r]

        total_area = 0

        while l < r:
            if height[l] <= height[r]:
                l+=1
                l_max = max(height[l],l_max)
                total_area += (l_max - height[l])
            else:
                r-=1
                r_max = max(height[r],r_max)
                total_area += (r_max - height[r])

        return total_area