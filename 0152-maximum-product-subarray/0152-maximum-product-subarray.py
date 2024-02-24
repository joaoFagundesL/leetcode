class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
          return nums[0]
        
        min_dp = [float('inf')] * n
        max_dp = [float('-inf')] * n
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]
        
        for i in range(1, n):
          c1 = min_dp[i - 1] * nums[i]
          c2 = max_dp[i - 1] * nums[i]
          min_dp[i] = min(c1, c2, nums[i])
          max_dp[i] = max(c1, c2, nums[i])
        return max(max_dp)

        
          
        