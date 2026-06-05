class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            l = [0] * 26
            for j in i:
                l[ord(j)-97]+=1
            d[tuple(l)].append(i)
        return list(d.values())