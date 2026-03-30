class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]

        for i in range(len(nums)):

            current_total = 0
            for j in range(i, len(nums)):

                current_total += nums[j]

                answer = max(answer, current_total)
        
        return answer