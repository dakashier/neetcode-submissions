class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        for x in d:
            if d[x]>1:
                count+=1
                return True
        
        if count==0:
            return False

    
        