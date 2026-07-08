class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k

        res = []

        while r <= len(nums):
            current = max(nums[l:r])
            res.append(current)
            l += 1
            r += 1

        return res