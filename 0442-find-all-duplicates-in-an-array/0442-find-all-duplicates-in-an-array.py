class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            x = abs(nums[i])
            idx = x - 1
            
            if nums[idx] < 0:
                ans.append(idx + 1)
            else:
                nums[idx] = nums[idx] * -1
        return ans
                