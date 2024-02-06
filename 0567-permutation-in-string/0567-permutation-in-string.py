class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len =  len(s1), len(s2)                                                         
    
        if s1_len > s2_len or s2_len == 0: return False
        if s1_len == 0: return True 
        
        hash_map_s1, hash_map_s2 = Counter(s1), Counter(s2[:s1_len])
        if hash_map_s1 == hash_map_s2: return True
        
        for idx in range(s1_len, s2_len):
            hash_map_s2[s2[idx]] += 1 
            hash_map_s2[s2[idx - s1_len]] -= 1
            
            if hash_map_s2 == hash_map_s1: return True
        
        return False
