class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for idx,num in enumerate(nums):
            answer = target - num
            if answer in num_index:
                return [num_index[answer], idx]
            else:
                num_index[num] = idx


