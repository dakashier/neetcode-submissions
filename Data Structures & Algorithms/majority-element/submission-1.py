class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        res = 0
        cur = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for (i, j) in d.items():
            if j > cur:
                cur = j
                res = i
            
        return res