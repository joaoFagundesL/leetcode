class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans, maxx, my_hash, len_nums = 0, 0, Counter(nums), len(nums)
        
        for k, v in my_hash.items(): maxx = max(maxx, v)
        if maxx == 1: return len_nums
        
        for k, v in my_hash.items():
            if maxx == v:
                ans += 1
        return ans * maxx
        