class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = nums[0]
        
        for i in range(1, n):
            ans[i] = ans[i - 1] + nums[i]
        return ans