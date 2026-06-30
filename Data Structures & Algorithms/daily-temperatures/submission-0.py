class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        j = 0
        while j < len(temperatures):
            for i in range(j, len(temperatures) + 1):
                if i == len(temperatures):
                    result.append(0)
                
                elif temperatures[j] < temperatures[i]:
                    result.append(i - j)
                    break
            j += 1
        return result