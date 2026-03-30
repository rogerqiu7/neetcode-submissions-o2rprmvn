class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        max_count = 0
        answer = None

        for key,value in counter.items():
            if value > max_count:
                max_count = value
                answer = key

        return answer