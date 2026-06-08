class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-1):
            st = -(nums[i])
            f = i + 1
            l = len(nums) - 1

            while f<l:
                CurSum = nums[f] + nums[l]
                if CurSum > st:
                    l -=1
                if CurSum < st:
                    f +=1
                if CurSum == st:
                    if [nums[i], nums[f], nums[l]] not in result:
                        result.append([nums[i], nums[f], nums[l]])
                    f += 1
                    l -= 1
        return result