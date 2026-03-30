class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = k - 1

        while r < len(nums):
            current_max = max(nums[l:r+1])
            res.append(current_max)

            l += 1
            r += 1

        return res