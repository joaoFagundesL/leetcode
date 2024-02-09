class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_size, ans, max_heap = len(nums), [], []
        
        for idx in range(k):
            heappush(max_heap, -1 * nums[idx])
            
        removed = {}
        ans.append(max_heap[0] * -1)
        
        for idx in range(k, nums_size):
            heappush(max_heap, -1 * nums[idx])
            removed[nums[idx - k]] = removed.get(nums[idx - k], 0) + 1
            while max_heap[0] * -1 in removed and removed[max_heap[0] * -1] > 0:
                removed[max_heap[0] * -1] -= 1
                heappop(max_heap)
            ans.append(max_heap[0] * -1)
            
        return ans;
            