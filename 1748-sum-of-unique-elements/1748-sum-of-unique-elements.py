class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c)
        
        ans = 0
        for k, v in c.items():
            if v == 1:
                ans += k
        return ans