class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        if not nums:
            return 0
        
        max_streak = 1

        current = 1

        for i in range(len(nums)):

            if nums[i] == nums[i-1]+1:
                current += 1
            else:
                current = 1

            max_streak = max(current, max_streak)

        return max_streak
            


