class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 1: return 1
        if len_s == 0: return 0
        
        hash_set, ans, start, end = set(), 0, 0, 0
       
        while end < len_s:
            while s[end] in hash_set:
                hash_set.remove(s[start])
                start += 1
                
            hash_set.add(s[end])
            ans = max(ans, end - start + 1)
            end += 1   
        return ans