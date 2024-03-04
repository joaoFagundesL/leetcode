class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        
        for e in nums:
            heapq.heappush(heap, e)
        
        ans = 0
        for _ in range(n):
            if heap[0] < k:
                heapq.heappop(heap)
                ans += 1
            else:
                return ans
        return ans