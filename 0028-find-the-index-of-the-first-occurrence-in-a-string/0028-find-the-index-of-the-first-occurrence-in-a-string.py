# NAIVE SOLUTION | TIME COMPLEXITY  O(m * n)
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#       len_haystack, len_needle = len(haystack), len(needle)
#       # sadbutsad => no need to start the index from index 7 because the len of
#       # needle would be greater and i wont find waht im looking for
#       valid_len = len_haystack + 1 - len_needle
      
#       for idx in range(valid_len):
#         for j in range(len_haystack):
#           # idx + j means i'm going forward in the haystack because idx only iterates one time
#           # for all values of j
#           if haystack[idx + j] != needle[j]:
#             break
#           if j == len_needle - 1:
#             return idx
#       return -1
    
# KMP SOLUTION | TIME COMPLEXITY  O(m + n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      # LPS ARRAY
      N, M = len(haystack), len(needle)
      lsp = [0] * M
      lsp[0] = 0
      prev, i = 0, 1
      while i < M:
        if needle[prev] == needle[i]:
          lsp[i] = prev + 1
          prev, i = prev + 1, i + 1
        elif prev == 0:
            lsp[i] = 0
            i += 1
        else:
          prev = lsp[prev - 1]
      
      # KMP
      valid_starting, j, k = N + 1 - M, 0, 0
      while j < N:
        if haystack[j] == needle[k]:
          j, k = j + 1, k + 1
        elif k != 0:
          k = lsp[k - 1]
        else:
          j += 1
        if k == M:
          return j - k
          # k = lsp[k - 1] => look for more occurrences
      return -1
      
      
          
          
          