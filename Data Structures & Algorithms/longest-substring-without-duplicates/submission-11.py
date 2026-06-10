class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = [0]
        e = ''
        i = 0
        j = 0

        while i < len(s):
            if len(s) == 1:
                return 1
            if s[i] in e:
                j += 1
                i = j
                l.append(len(e))
                e = ''
            else:
                e += s[i]
                i += 1
        l.append(len(e))
        l.sort()
        return l[-1]