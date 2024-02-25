class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums)
        length = len(nums)      
        new_length = length / 2
        
        for v in count.values():
            if v > 2: return False
        return True
            
        
        
        