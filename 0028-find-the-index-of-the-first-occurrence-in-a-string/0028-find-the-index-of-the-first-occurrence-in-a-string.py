class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      len_haystack, len_needle = len(haystack), len(needle)
     
      for idx in range(len_haystack):
        if len_haystack - idx < len_needle:
          return -1
        else:
          for j in range(len_haystack):
            # idx + j means i'm going forward in the haystack because idx only iterates one time
            # for all values of j
            if haystack[idx + j] != needle[j]:
              break
            if j == len_needle - 1:
              return idx
      return -1