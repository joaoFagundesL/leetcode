class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, ans, nums_size = collections.deque(), [], len(nums)
        
        start, end = 0, k
        for idx in range(k):
            while deq and nums[deq[-1]] < nums[idx]:
                deq.pop()    
            deq.append(idx) 
            
        ans.append(nums[deq[start]])
        
        while end < nums_size:
            if deq and deq[0] <= start:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[end]:
                deq.pop() 
            deq.append(end)
            ans.append(nums[deq[0]])
            start += 1
            end += 1
        return ans
        
                
            