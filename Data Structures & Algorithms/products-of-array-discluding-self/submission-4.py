class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for num in nums]

        if nums.count(0) == 1:
            total_sum = 1

            for num in nums:
                if num != 0:
                    total_sum *= num

            answer = []

            for num in nums:
                if num != 0:
                    answer.append(0)
                else:
                    answer.append(total_sum)

            return answer

        answer = []

        total = 1
        for num in nums:
            total *= num

        for num in nums:

            answer.append(total//num)

        return answer