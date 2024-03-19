class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_size = len(nums)
        curr = nums[0]
        total = nums[0]
        max_sum = nums[0]
        l, r = 0, 0
        max_left, max_right = 0, 0

        for i in range(1, nums_size):
            # expand to the right
            if curr + nums[i] > nums[i]:
                r = i
                curr = curr + nums[i]
            else:
                # found new starting subarray
                l = r = i
                curr = nums[i]

            if curr > total:
                # save the l and r before continue
                total = curr
                max_left, max_right = l, r

        # also returning the subarray
        print(nums[max_left:max_right + 1])
        return total