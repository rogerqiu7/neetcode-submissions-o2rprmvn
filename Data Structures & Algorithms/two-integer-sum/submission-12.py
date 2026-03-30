class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index_dict = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in number_index_dict:
                return [number_index_dict[diff], index]

            number_index_dict[number] = index