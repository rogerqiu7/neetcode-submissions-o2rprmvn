class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:
            total = 1
            for num in nums:
                if num != 0:
                    total *= num
            return [0 if num != 0 else total for num in nums]

        total = 1
        for num in nums:
            total *= num
         
        answer = []
        for num in nums:
            total_divided = total // num
            answer.append(total_divided)
        return answer