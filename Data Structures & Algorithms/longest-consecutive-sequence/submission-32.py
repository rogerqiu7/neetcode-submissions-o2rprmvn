class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        counter = 1
        max_count = 1

        nums = sorted(list(set(nums)))

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                counter += 1
            else:
                counter = 1

            max_count = max(counter, max_count)

        return max_count