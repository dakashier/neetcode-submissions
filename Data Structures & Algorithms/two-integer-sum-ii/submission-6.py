class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1
        
        while f < l:
            CurSum = numbers[f] + numbers[l]
            if CurSum < target:
                f += 1
            if CurSum > target:
                l -= 1
            if CurSum == target:
                return [f+1, l+1]