class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = {}
        max_freq, ans, count = -1, [], 0 

        for e in nums:
            counter[e] = counter.get(e, 0) + 1
            max_freq = max(max_freq, counter[e])

        freq =[[] for _ in range(max_freq + 1)]
        
        for key, val in counter.items(): freq[val].append(key)
        
        for i in range(max_freq, 0, -1):
            for val in freq[i]:
                count += 1
                ans.append(val)
                if count == k: return ans

