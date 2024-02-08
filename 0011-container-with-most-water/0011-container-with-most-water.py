class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, l, r = 0, 0, len(height) - 1
        
        while l < r:
            a = min(height[l], height[r]) * (r - l)
            ans = max(a, ans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans