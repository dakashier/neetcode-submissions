class Solution:
    def validPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s)-1
        while first<last:
            if s[first] != s[last]:
                skipfirst = s[first + 1 : last + 1]
                skiplast = s[first : last]
                return (skiplast == skiplast[::-1] or skipfirst == skipfirst[::-1])
            first+=1
            last-=1
        return True