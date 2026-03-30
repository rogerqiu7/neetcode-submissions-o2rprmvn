class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        counter_list = []

        for num, freq in counter.items():
            counter_list.append([freq,num])

        counter_list.sort()

        answer = []

        while len(answer) < k:
            answer.append(counter_list.pop()[1])

        return answer