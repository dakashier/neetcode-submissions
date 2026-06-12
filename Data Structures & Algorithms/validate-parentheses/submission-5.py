class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        openstuff = ['(','[','{']
        d = {')':'(',']':'[','}':'{'}

        if s[0] in d:
            return False
        
        stack = []
        for i in range(len(s)):
            if s[i] in openstuff:
                stack.append(s[i])
            else:
                if stack != []:
                    if stack[-1] != d[s[i]]:
                        return False
                    else:
                        stack.pop()
        return stack==[]