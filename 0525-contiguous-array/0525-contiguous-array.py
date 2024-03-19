class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total, ans, mp = 0, 0, {}
        
        for i, e in enumerate(nums):
            total += -1 if e == 0 else 1
            if total == 0:
                ans = max(ans, i + 1)
            elif total in mp:
                ans = max(ans, i - mp[total])
            else:
                mp[total] = i
        return ans