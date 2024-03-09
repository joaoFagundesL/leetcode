class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x = set()
        for e in nums1:
            x.add(e)
        for e in nums2:
            if e in x:
                return e
        return -1