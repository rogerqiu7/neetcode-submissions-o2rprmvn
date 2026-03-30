class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)

        nums = sorted(nums)

        for i in range(count):
            if nums[i] != i:
                return i
                
        return count