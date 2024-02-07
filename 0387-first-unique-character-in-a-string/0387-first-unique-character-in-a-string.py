class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_hash, len_s = {}, len(s)
        
        for idx, char in enumerate(s):
            if char not in my_hash:
                my_hash[char] = [idx, 1]
            else:
                my_hash[char][1] += 1
        
        for char, arr in my_hash.items():
            if arr[1] == 1:
                return arr[0]
        
        return -1
            
            