class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        num_list = []

        for num, freq in counter.items():
            num_list.append([freq, num])
        num_list.sort()

        answer = []
        while len(answer) < k:
            answer.append(num_list.pop()[1])

        return answer