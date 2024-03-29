class Solution:
  # O(logn)
#     def isPowerOfTwo(self, n: int) -> bool:
#       if n == 0:
#         return False
      
#       while True:
#         if n == 1:
#           return True
#         elif n % 2 != 0:
#           return False
#         n /= 2

# O(1)
    def isPowerOfTwo(self, n: int) -> bool:
      if n == 0:
        return False
      return n & (n - 1) == 0
