class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = sorted(list(set(nums)))

        answer = 1
        counter = 1

        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                counter += 1
            else:
                counter = 1
            answer = max(answer, counter)

        return answer
