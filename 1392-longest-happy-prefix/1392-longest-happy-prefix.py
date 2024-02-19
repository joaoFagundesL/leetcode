class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        lps = [0] * N
        lps[0] = 0
        prev, i = 0, 1
        while i < N:
          if s[i] == s[prev]:
            lps[i] = prev + 1
            prev, i = prev + 1, i + 1
          elif prev == 0:
            lps[i] = 0
            i += 1
          else:
            prev = lps[prev - 1]
        return s[:lps[-1]]
      
      # aabaaac 
      # prefix: a, aa, aab, aaba, aabaa, abaaa..
      # sufix: c, ca, caa, caaab
      # lps = [0,1,0,1,2,2,0] => as long as i have two i'll take always the [-1]