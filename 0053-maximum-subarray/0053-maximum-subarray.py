class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_size = len(nums)
        dp = [0] * nums_size
        dp[0] = nums[0]
        
        for i in range(1, nums_size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
      
        return max(dp)