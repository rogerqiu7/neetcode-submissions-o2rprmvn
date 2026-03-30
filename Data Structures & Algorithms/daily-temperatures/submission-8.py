class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            found = False
            current_count = 0
            for j in range(i+1, len(temperatures)):
                current_count += 1
                if temperatures[j] > temperatures[i]:
                    found = True
                    res.append(current_count)
                    break
 
            if found == False:
                res.append(0)

        return res
