class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums_len = len(nums)
        total, start, end, curr = 0, 0, 0, float('inf')
        
        # O(n) solution
        while end < nums_len:
          total += nums[end]
          while total >= target:
            curr = min(curr, end - start + 1)
            total -= nums[start]
            start += 1
          end += 1
              
        if curr == float('inf'): return 0
        else: return curr
      
       
      