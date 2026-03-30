class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        if zero_count == 1:

            total_product = 1

            for num in nums:
                if num != 0:
                    total_product *= num

            answer = []

            for num in nums:
                if num == 0:
                    answer.append(total_product)
                else:
                    answer.append(0)

            return answer
        
        total_product = 1

        for num in nums:
            total_product *= num

        answer = []
        for num in nums:
            answer.append(total_product // num)

        return answer