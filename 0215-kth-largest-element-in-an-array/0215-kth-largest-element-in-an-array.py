class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      nums_len, h = len(nums), []
      for idx in range(nums_len):
        heapq.heappush(h, nums[idx]) # min heap
        if len(h) > k:
          heapq.heappop(h)
      return heapq.heappop(h)
          
     
        
     
       
          