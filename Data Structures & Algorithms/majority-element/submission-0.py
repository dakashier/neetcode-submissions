class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        k=nums.count(nums[0])
        i=k
        j=nums[0]
        while i<len(nums):
            if nums.count(nums[i])>k:
                k=nums.count(nums[i])
                j=nums[i]
            i+=nums.count(nums[i])
        return j