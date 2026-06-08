class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        prefix = height[l]
        area = 0
        postfix = height[r]
        while l<r:
            if prefix < postfix:
                l += 1
                prefix = max(prefix, height[l])
                area += prefix - height[l]
            else:
                r -= 1
                postfix = max(postfix, height[r])
                area += postfix - height[r]
        return area