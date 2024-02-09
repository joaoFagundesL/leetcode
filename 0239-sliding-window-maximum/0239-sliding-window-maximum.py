class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, ans, nums_size = collections.deque(), [], len(nums)
        
        for idx in range(nums_size):
            # out of range for the current window
            while deq and deq[0] <= (idx - k):
                deq.popleft()
            # popping lesser values
            while deq and nums[deq[-1]] < nums[idx]:
                deq.pop()    
            deq.append(idx)
            
            if idx >= k - 1:
                ans.append(nums[deq[0]])
        return ans
                
            