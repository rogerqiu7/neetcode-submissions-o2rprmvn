class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(list(set(nums)))

        max_count = 1
        current_count = 1

        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                current_count += 1
            else:
                current_count = 1
            max_count = max(current_count, max_count)

        return max_count