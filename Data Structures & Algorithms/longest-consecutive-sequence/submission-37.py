class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        if not nums:
            return 0
        
        current = 1
        res = 1

        for i in range(len(nums) - 1):
            if (nums[i] + 1) == nums[i+1]:
                current += 1
                res = max(res, current)
            else:
                current = 1

        return res

