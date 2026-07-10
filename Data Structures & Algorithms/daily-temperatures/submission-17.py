class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        index_stack = []

        for i in range(len(temperatures)):
            while index_stack and temperatures[i] > temperatures[index_stack[-1]]:
                previous_index = index_stack.pop()
                res[previous_index] = i - previous_index
            index_stack.append(i)

        return res