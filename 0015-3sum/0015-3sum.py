class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len, ans = len(nums), []
        
        nums.sort()
        
        for idx, val in enumerate(nums):
            # i have just checked the possibilities for the value, if it is the same
            # there is no need to do it again because i'll get the same result
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            # use the same approach from two sum array sorted, here just setting the pointers
            l, r = idx + 1, nums_len - 1
            
            while l < r:
                three_sum = val + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    ans.append([val, nums[l], nums[r]])
                    # now that i found an answer I'll move the pointer to the left
                    # to continue searching for another possible solution. However, 
                    # if it is the same value that i already checked it means it'll be
                    # the same solution hence i dont use it
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
                