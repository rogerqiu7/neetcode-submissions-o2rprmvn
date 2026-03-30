class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            # if found
            if nums[i] == target:
                return i
            # if not found, target is less than biggest
            if nums[i] > target:
                return i
        # if target is the biggest
        return len(nums)