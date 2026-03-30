class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        reversed_list = []

        for key, value in counter.items():
            reversed_list.append([value, key])

        reversed_list.sort()

        answer = []

        while len(answer) < k:
            answer.append(reversed_list.pop()[1])

        return answer

        