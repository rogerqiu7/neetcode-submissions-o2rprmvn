class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index_dict = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in value_index_dict:
                return [value_index_dict[diff], index]

            value_index_dict[value] = index