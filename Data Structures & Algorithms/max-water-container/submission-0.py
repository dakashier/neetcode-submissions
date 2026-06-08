class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        f = 0
        l = len(heights) - 1

        while f<l:
            narea = (l-f) * min(heights[f], heights[l])
            if narea>  area:
                area = narea
            if heights[f] > heights[l]:
                l -= 1
            else:
                f += 1
        return area