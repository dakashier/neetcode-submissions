class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        result = []
        while r < len(nums):
            lis = nums[l : r+1]
            lis.sort()
            result.append(lis[-1])
            l += 1
            r += 1
        return result