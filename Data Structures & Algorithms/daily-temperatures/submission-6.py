class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            found = False
            count = 0

            for j in range(i+1, len(temperatures)):
                count += 1

                if temperatures[j] >  temperatures[i]:
                    found = True
                    break
                
            if found == False:
                res.append(0)
            else:
                res.append(count)

        return res