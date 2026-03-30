class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        new_list = []
        for num, freq in counter.items():
            new_list.append([freq, num])
        new_list.sort()

        answer = []

        while len(answer) < k:
            answer.append(new_list.pop()[1])

        return answer  