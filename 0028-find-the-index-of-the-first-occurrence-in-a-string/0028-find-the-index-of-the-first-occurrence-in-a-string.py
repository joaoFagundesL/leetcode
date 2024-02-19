class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      len_haystack, len_needle = len(haystack), len(needle)
      # sadbutsad => no need to start the index from index 7 because the len of
      # needle would be greater and i wont find waht im looking for
      valid_len = len_haystack + 1 - len_needle
      
      for idx in range(valid_len):
        for j in range(len_haystack):
          # idx + j means i'm going forward in the haystack because idx only iterates one time
          # for all values of j
          if haystack[idx + j] != needle[j]:
            break
          if j == len_needle - 1:
            return idx
      return -1