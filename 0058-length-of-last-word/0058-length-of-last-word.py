class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() # remove trailing and leading space 
        len_s = len(s)
      
        if len_s == 0:
          return 0
        
        end = len_s - 1
        count = 0
        
        while end >= 0 and s[end] != " ":
          count += 1
          end -= 1
        return count
        