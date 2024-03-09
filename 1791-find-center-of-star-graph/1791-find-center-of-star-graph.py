class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = {}
        
        for v1, v2 in edges:
            freq[v1] = freq.get(v1, 0) + 1
            freq[v2] = freq.get(v2, 0) + 1
            
        n = len(freq)
        for k, v in freq.items():
            if v == n - 1:
                return k
        return -1
        
                    