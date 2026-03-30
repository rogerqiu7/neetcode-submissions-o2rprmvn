class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        answer = []

        for key,value in counter.items():
            if value > len(nums) // 3:
                answer.append(key)

        return answer