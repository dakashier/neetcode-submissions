class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        if s.isalnum()==True:
            if s==s[::-1]:
                return True
            else:
                return False
        else:
            s1=''
            for i in range(len(s)):
                if s[i].isalnum()==True:
                    s1=s1+s[i]
            if s1==s1[::-1]:
                return True
            else:
                return False