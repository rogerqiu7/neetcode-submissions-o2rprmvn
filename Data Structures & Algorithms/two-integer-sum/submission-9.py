class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_value_dict = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in number_value_dict:
                return [number_value_dict[diff], index]
            number_value_dict[number] = index
