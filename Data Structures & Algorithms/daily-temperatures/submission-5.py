class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_count = 0
        answer = []

        for i in range(len(temperatures)):
            found = False
            count = 0

            for j in range(i+1, len(temperatures)):
                count += 1

                if temperatures[j] > temperatures[i]:
                    found = True
                    break

            if found == False:
                answer.append(0)
            else:
                answer.append(count)

        return answer
