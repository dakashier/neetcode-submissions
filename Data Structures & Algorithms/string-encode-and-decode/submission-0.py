class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += i + '.'
        return s

    def decode(self, s: str) -> List[str]:
        result = s.split(".")
        result.pop()
        return result