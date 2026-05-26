class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        l = 0
        r = k

        while r <= len(nums):
            num = max(nums[l:r])
            res.append(num)
            l+=1
            r+=1
        return res