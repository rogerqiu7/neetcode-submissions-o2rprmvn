class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            found = False
            count = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    found = True
                    break
                else:
                    count += 1
            
            if found:
                res.append(count)
            else:
                res.append(0)

        return res
