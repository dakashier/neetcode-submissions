class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26

        l = 0
        r = len(s1) - 1

        for i in s1:
            s1_count[ord(i) - ord('a')] += 1

        while (l < len(s2)) and (r < len(s2)):
            temp = [0] * 26
            s = s2[l : r + 1]
            for i in s:
                temp[ord(i) - ord('a')] += 1
            if temp == s1_count:
                return True
            l += 1
            r += 1
        return False