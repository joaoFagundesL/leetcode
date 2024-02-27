class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = [0] * len(arr)
        h = {}
        count = 0
        
        for i, w in enumerate(arr):
            if w not in h:
                h[w] = i
                freq[i] = 1
            else:
                freq[h[w]] += 1
        
        count = 0
        for i, a in enumerate(freq):
            if a == 1:
                count += 1
                if count == k:
                    return arr[i]
        return ""
            
        