class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[]
        l2=[]
        for i in range(len(s)):
            l1.append(s[i])
        for j in range(len(t)):
            l2.append(t[j])
        l1=sorted(l1)
        l2=sorted(l2)
        if l1==l2:
            return True
        else:
            return False

        