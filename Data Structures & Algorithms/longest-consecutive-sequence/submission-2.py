class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current = 1
        max_streak = 1

        nums = sorted(set(nums))

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1

            max_streak = max(max_streak, current)

        return max_streak