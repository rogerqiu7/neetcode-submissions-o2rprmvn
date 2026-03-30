class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []

        for i in range(len(temperatures)):
            found = False

            for j in range(i+1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    days = j - i
                    answer.append(days)
                    found = True
                    break
                

            if not found:
                answer.append(0)

        return answer