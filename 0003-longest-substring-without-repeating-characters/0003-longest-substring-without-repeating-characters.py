class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 1: return 1
        if len_s == 0: return 0
        
        curr, hash_set, m, start, end = 1, set(), 1, 0, 1
        hash_set.add(s[0])
        while end < len_s:
            if s[end] in hash_set:
                start += 1
                hash_set.clear()
                hash_set.add(s[start])
                end = start + 1
                curr = 1
            else:
                hash_set.add(s[end])
                curr += 1
                end += 1
                if curr > m:
                    m = curr
                    if m > end - start + 1:
                        return m        
        return m