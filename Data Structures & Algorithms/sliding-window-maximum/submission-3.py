class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        k = k - 1

        while k < len(nums):
            subList = nums[l:k+1]
            res.append(max(subList))
            l +=1
            k +=1

        return res