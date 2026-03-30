class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in value_index_dict:
                other_value = target - nums[i]
                return [value_index_dict[other_value], i]
            else:
                value_index_dict[nums[i]] = i