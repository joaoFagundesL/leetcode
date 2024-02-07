class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_nums1, hash_nums2 = Counter(nums1), Counter(nums2)
        len_nums1, len_nums2 = len(nums1), len(nums2)
        
        ans = [0, 0]
        
        for idx in range(len_nums1):
            if nums1[idx] in hash_nums2:
                ans[0] += 1
                
        for idx in range(len_nums2):
            if nums2[idx] in hash_nums1:
                ans[1] += 1
        return ans
        