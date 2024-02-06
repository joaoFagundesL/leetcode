class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map_s1, hash_map_s2, s1_len, s2_len = {}, {}, len(s1), len(s2)
        
        if s1_len > s2_len or s2_len == 0: return False
        if s1_len == 0: return True
        
        for idx in range(s1_len):
            hash_map_s1[s1[idx]] = hash_map_s1.get(s1[idx], 0) + 1
            hash_map_s2[s2[idx]] = hash_map_s2.get(s2[idx], 0) + 1   
        
        for idx in range(s1_len, s2_len):
            if self.compareHash(hash_map_s1, hash_map_s2):
                return True 
            hash_map_s2[s2[idx]] = hash_map_s2.get(s2[idx], 0) + 1 
            hash_map_s2[s2[idx - s1_len]] -= 1
        return self.compareHash(hash_map_s1, hash_map_s2)
    
    def compareHash(self, map1, map2):
        for k in map1:
            if k not in map2 or map1[k] != map2[k]: 
                return False
        return True
