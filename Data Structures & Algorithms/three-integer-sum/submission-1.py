class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        combo = [nums[i], nums[j], nums[k]]
                        if sorted(combo) not in answer:
                            answer.append(sorted(combo))

        return answer