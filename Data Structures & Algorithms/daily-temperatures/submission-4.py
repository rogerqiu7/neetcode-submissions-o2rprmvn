class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []

        for i in range(len(temperatures)):
            count = 0
            found = False

            for j in range(i+1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    found = True
                    break
                    
            if found:
                answer.append(count)
            else:
                answer.append(0)

        return answer