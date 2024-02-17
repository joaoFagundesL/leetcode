class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len <= 2:
          return nums_len
          
        a = 2
        for idx in range(2, nums_len):
          if nums[idx] != nums[a - 2]:
            nums[a] = nums[idx]
            a += 1
        return a