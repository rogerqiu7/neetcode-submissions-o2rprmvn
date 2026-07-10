class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            counter = 0
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    counter += 1
                    found = True
                    break
                else:
                    counter += 1
            if found:
                res.append(counter)
            else:
                res.append(0)

        return res 
